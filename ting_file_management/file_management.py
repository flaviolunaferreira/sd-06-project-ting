import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")

    try:
        fileObject = open(path_file, "r")
    except Exception:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return 0
    data = fileObject.read()
    return data.split("\n")
