import sys


# https://www.w3schools.com/python/ref_string_splitlines.asp
def txt_importer(path_file):
    
    if not path_file.endswith('.txt'):
        sys.stderr.write('Formato inválido')
    try:
        lines = ''
        with open(path_file) as file:
            lines = file.read().splitlines()
        return lines
    except:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
