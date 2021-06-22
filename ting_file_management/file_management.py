import sys
import os.path


def txt_importer(path_file):
    is_txt = path_file.endswith('txt')
    is_path = os.path.isfile(path_file)

    if not is_txt:
        return sys.stderr.write('Formato inválido\n')
    elif not is_path:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
    else:
        text = []
        with open(path_file) as file:
            for line in file:
                text.append(line.replace('\n', ''))

        return text
