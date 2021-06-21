import sys


# https://www.w3schools.com/python/ref_string_splitlines.asp
def txt_importer(path_file):
    if path_file:
        lines = ''
        if not path_file.endswith('.txt'):
            sys.stderr.write('Formato inválido')
        with open(path_file) as file:
            lines = file.read().splitlines()
        return lines
    else:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
