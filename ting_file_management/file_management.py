import os
import sys


def txt_importer(path_file):
    if (not os.path.exists(path_file)):
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

    extension = path_file.split('.')[-1]
    if (extension != 'txt'):
        return print("Formato inválido", file=sys.stderr)

    with open(path_file, 'r') as file:
        txt = file.read().split('\n')
    return txt
