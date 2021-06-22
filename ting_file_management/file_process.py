import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    length = instance.__len__()
    if (length == 0):
        file_read = txt_importer(path_file)
        lines = len(file_read)
        instance.enqueue(path_file)
        formated_info = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": lines,
            "linhas_do_arquivo": file_read
        }
    sys.stdout.write(f"{formated_info}\n")


def remove(instance):
    """Aqui irá sua implementação"""
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")
    instance.dequeue()
    sys.stdout.write(
        'Arquivo statics/arquivo_teste.txt removido com sucesso\n'
    )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    if (position > instance.__len__() - 1 or position < 0):
        sys.stderr.write('Posição inválida')
