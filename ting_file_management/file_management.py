import sys


# https://www.w3schools.com/python/ref_string_splitlines.asp
def txt_importer(path_file):

    if not path_file.endswith('.txt'):
        sys.stderr.write('Formato inválido')
    try:
        file = open(path_file)
        return file.read().splitlines()
    except ValueError:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
