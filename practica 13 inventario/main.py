import sys
import json
import re
from antlr4 import *
from generated.CSVLexer import CSVLexer
from generated.CSVParser import CSVParser
from generated.CSVListener import CSVListener


class ValidatedRow:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"ValidatedRow(data={self.data})"


class Loader(CSVListener):
    def __init__(self):
        self.header = []  # Nombres de las columnas
        self.intermediate_representation = []
        self.semantic_errors = []
        self.currentRowFieldValues = []
        self.line_counter = 0
        self.ids_vistos = set()  # Para detectar IDs duplicados

    def enterRow(self, ctx: CSVParser.RowContext):
        self.currentRowFieldValues = []
        self.line_counter += 1

    def exitRow(self, ctx: CSVParser.RowContext):
        if self.line_counter == 1:
            self.header = [v.strip() for v in self.currentRowFieldValues]
            return

        line = ctx.start.line

        # Validar número de columnas
        if len(self.currentRowFieldValues) != len(self.header):
            self.semantic_errors.append({
                "linea": line,
                "error": "Número incorrecto de columnas",
                "descripcion": f"La fila tiene {len(self.currentRowFieldValues)} columnas, se esperaban {len(self.header)}."
            })
            return

        row_dict = {}
        fila_valida = True

        for i, val in enumerate(self.currentRowFieldValues):
            key = self.header[i]
            cleaned_val = val.strip() if isinstance(val, str) else val

            # 1. Validar campos vacíos
            if cleaned_val == "":
                self.semantic_errors.append({
                    "linea": line,
                    "error": "Campo vacío",
                    "descripcion": f"El campo '{key}' está vacío."
                })
                fila_valida = False
                continue

            # 2. Validar codificación inválida (caracteres mal codificados)
            if re.search(r"[ÃÂ¢Ã³Ã¡Ã±]", cleaned_val):
                self.semantic_errors.append({
                    "linea": line,
                    "error": "Codificación inválida",
                    "descripcion": f"El campo '{key}' contiene caracteres no válidos o mal codificados: '{cleaned_val}'."
                })
                fila_valida = False

            # 3. Validar tipo numérico
            if key.lower() in ["precio", "stock"]:
                try:
                    valor = float(cleaned_val)
                    # 4. Validar que sean positivos
                    if valor <= 0:
                        self.semantic_errors.append({
                            "linea": line,
                            "error": "Valor no permitido",
                            "descripcion": f"El campo '{key}' debe ser positivo. Valor encontrado: {valor}."
                        })
                        fila_valida = False
                    # 5. Validar stock fuera de rango
                    if key.lower() == "stock" and (valor < 0 or valor > 1000):
                        self.semantic_errors.append({
                            "linea": line,
                            "error": "Stock fuera de rango",
                            "descripcion": f"El stock '{valor}' no es válido (rango permitido: 0–1000)."
                        })
                        fila_valida = False
                except ValueError:
                    self.semantic_errors.append({
                        "linea": line,
                        "error": "Valor no numérico",
                        "descripcion": f"El campo '{key}' contiene un valor no numérico: {cleaned_val}"
                    })
                    fila_valida = False
                    continue

            #  6. Validar longitud de texto
            if key.lower() == "producto" and len(cleaned_val) > 80:
                self.semantic_errors.append({
                    "linea": line,
                    "error": "Texto demasiado largo",
                    "descripcion": f"El campo '{key}' supera los 80 caracteres ({len(cleaned_val)})."
                })
                fila_valida = False

            row_dict[key] = cleaned_val

        # 7. Validar formato de ID
        if fila_valida and "ID" in row_dict:
            id_val = row_dict["ID"]
            if not re.match(r"^SKU-\d{3,}$", id_val):
                self.semantic_errors.append({
                    "linea": line,
                    "error": "Formato de ID inválido",
                    "descripcion": f"El ID '{id_val}' no cumple con el formato esperado 'SKU-###'."
                })
                fila_valida = False

            # 8. Validar ID duplicado
            if id_val in self.ids_vistos:
                self.semantic_errors.append({
                    "linea": line,
                    "error": "ID duplicado",
                    "descripcion": f"El ID '{id_val}' ya fue registrado previamente."
                })
                fila_valida = False
            else:
                self.ids_vistos.add(id_val)

        if fila_valida:
            self.intermediate_representation.append(ValidatedRow(row_dict))

    def exitText(self, ctx: CSVParser.TextContext):
        text = ctx.getText().strip()
        if text.count('"') == 1:
            line = ctx.start.line
            self.semantic_errors.append({
                "linea": line,
                "error": "Comillas sin cerrar",
                "descripcion": f"El campo '{text}' contiene una comilla de apertura sin cierre."
            })
        self.currentRowFieldValues.append(text)

    def exitString(self, ctx: CSVParser.StringContext):
        text = ctx.getText()
        if not (text.startswith('"') and text.endswith('"')):
            line = ctx.start.line
            self.semantic_errors.append({
                "linea": line,
                "error": "Comillas sin cerrar",
                "descripcion": f"El campo '{text}' no cierra las comillas correctamente."
            })
        text = text[1:-1].replace('""', '"')
        self.currentRowFieldValues.append(text)

    def exitEmpty(self, ctx: CSVParser.EmptyContext):
        self.currentRowFieldValues.append("")


def main(argv):
    input_stream = FileStream(argv[1], encoding='utf-8')
    lexer = CSVLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CSVParser(stream)
    tree = parser.csvFile()

    loader = Loader()
    walker = ParseTreeWalker()
    walker.walk(loader, tree)

    #  Mostrar errores semánticos
    if loader.semantic_errors:
        print("\n--- ERRORES SEMÁNTICOS DETECTADOS ---")
        for err in loader.semantic_errors:
            print(f"Línea {err['linea']} | {err['error']}: {err['descripcion']}")
    else:
        print("\n✅ No se detectaron errores semánticos.")

    #  Mostrar representación intermedia
    print("\n--- REPRESENTACIÓN INTERMEDIA GENERADA ---")
    for row in loader.intermediate_representation:
        print(row)

    #  Exportar a JSON
    json_output = [row.data for row in loader.intermediate_representation]
    with open("intermediate_representation.json", "w", encoding="utf-8") as f:
        json.dump(json_output, f, indent=4)
    print("\nArchivo JSON generado: intermediate_representation.json")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo_csv>")
    else:
        main(sys.argv)
