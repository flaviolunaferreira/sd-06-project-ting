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
    length = instance.__len__()
    if length <= 0:
        return sys.stdout.write('Não há elementos\n')
    instance.dequeue()
    # arquivo hardcoded, como retornar o path_file?
    sys.stdout.write(
        'Arquivo statics/arquivo_teste.txt removido com sucesso\n'
    )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
