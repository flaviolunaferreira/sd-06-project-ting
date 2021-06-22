import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    file = txt_importer(path_file)
    for item in file:
        instance.enqueue(item)
    length = instance.__len__()
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": length,
        "linhas_do_arquivo": file
    }
    sys.stdout.write(f"{result}\n")


def remove(instance):
    """Aqui irá sua implementação"""
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")
    removed_file = instance.dequeue()
    return sys.stdout.write(f"Arquivo {removed_file} removido com sucesso\n")

def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    if (position > instance.__len__() - 1 or position < 0):
        sys.stderr.write('Posição inválida')
