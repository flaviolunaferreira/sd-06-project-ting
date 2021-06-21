import sys
import os.path


def txt_importer(path_file):
    isTxt = path_file.endswith(".txt")
    exist = os.path.isfile(path_file)
    if not isTxt:
        return sys.stderr.write("Formato inválido\n")
    if not exist:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    with open(path_file, 'r') as file:
        conteudo = file.read().splitlines()
        return conteudo
