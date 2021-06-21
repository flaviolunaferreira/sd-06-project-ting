import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    for item in file:
        instance.enqueue(item)
    file_length = instance.__len__()
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": file_length,
        "linhas_do_arquivo": file
    }
    sys.stdout.write(f"{result}\n")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
