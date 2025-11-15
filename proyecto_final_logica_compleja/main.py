import sys
import os
import io
from contextlib import redirect_stdout
from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from generated.logicaLexer import logicaLexer
from generated.logicaParser import logicaParser
from semantic_analyzer.SemanticVisitor import SemanticVisitor
from codegen.PythonGenerator import PythonCodeGenerator


class CollectingErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Error de sintaxis {line}:{column} {msg}")


def basename_from(path):
    return os.path.splitext(os.path.basename(path))[0] or "programa"


def write_text(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    # -------- rutas --------
    input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    out_dir = "output_python"
    os.makedirs(out_dir, exist_ok=True)
    out_log = "output.txt"

    # -------- fase léxica / sintáctica --------
    err_lexer = CollectingErrorListener()
    err_parser = CollectingErrorListener()

    try:
        fs = FileStream(input_path, encoding="utf-8")
    except Exception as e:
        msg = f"[ARCHIVO]\nNo se pudo leer '{input_path}': {e}\n"
        write_text(out_log, msg)
        print(msg, end="")
        return

    lexer = logicaLexer(fs)
    lexer.removeErrorListeners()
    lexer.addErrorListener(err_lexer)

    stream = CommonTokenStream(lexer)
    parser = logicaParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(err_parser)

    try:
        tree = parser.program()
    except Exception as e:
        msg = f"[SINTAXIS]\n{e}\n"
        write_text(out_log, msg)
        print(msg, end="")
        return

    if err_lexer.errors or err_parser.errors:
        partes = []
        if err_lexer.errors:
            partes.append("[LEXICO]")
            partes += err_lexer.errors
        if err_parser.errors:
            partes.append("[SINTAXIS]")
            partes += err_parser.errors
        texto = "\n".join(partes) + "\n"
        write_text(out_log, texto)
        print(texto, end="")
        return

    # -------- fase semántica --------
    visitor = SemanticVisitor()
    sem_buf = io.StringIO()
    with redirect_stdout(sem_buf):
        visitor.visit(tree)
    sem_out = sem_buf.getvalue().strip()

    # Si hubo mensajes semánticos (errores), no generamos código
    if sem_out:
        texto = "[SEMANTICO]\n" + sem_out + "\n"
        write_text(out_log, texto)
        print(texto, end="")
        return

    gen = PythonCodeGenerator()
    py_code = gen.generate_from_tac(visitor.ir.instructions)

    base = basename_from(input_path)
    out_py = os.path.join(out_dir, f"{base}.py")
    write_text(out_py, py_code)

    # éxito: no se escribe output.txt; solo anunciamos por consola
    print(f"[OK] Generado: {out_py}")


if __name__ == "__main__":
    main()
