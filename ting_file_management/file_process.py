from os import path
import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_content = txt_importer(path_file)
    for line in file_content:
        instance.enqueue(line)
    file_lines = instance.__len__()
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": file_lines,
        "linhas_do_arquivo": file_content
    }

    sys.stdout.write(str(result))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
