import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith('.txt'):
        sys.stderr.write('Formato inválido')
    try:
        file = open(path_file, "r")
        return file.read().splitlines()
    except FileNotFoundError:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
