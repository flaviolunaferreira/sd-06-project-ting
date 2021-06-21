import os.path
import sys


def txt_importer(path_file):
    if not os.path.isfile(path_file):
        return sys.stderr.write(
            f"Arquivo {path_file} não encontrado\n"
        )

    if path_file.split('.')[1] != "txt":
        return sys.stderr.write("Formato inválido\n")

    file = open(path_file, mode="r")
    content = file.read().splitlines()
    return content
