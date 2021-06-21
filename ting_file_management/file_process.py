from ting_file_management.file_management import txt_importer
import sys

def process(path_file, instance):
    file = txt_importer(path_file)
    for line in file:
        instance.enqueue(line)
    line_qtd = instance.__len__()
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": line_qtd,
        "linhas_do_arquivo": file
    }
    sys.stdout.write(f'{result}\n')

def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
