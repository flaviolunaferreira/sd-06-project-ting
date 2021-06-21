import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    text = txt_importer(path_file)
    output = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text),
        "linhas_do_arquivo": text
    }
    sys.stdout.write(f"{output}\n")
    return instance.enqueue(output)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
