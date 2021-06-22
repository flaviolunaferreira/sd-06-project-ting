import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if instance.__len__() < 1:
        file = txt_importer(path_file)
        result = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file
        }
        sys.stdout.write(str(result))
        instance.enqueue(result)


def remove(instance):
    length = instance.__len__()
    if length <= 0:
        return sys.stdout.write('Não há elementos\n')
    deq = instance.dequeue()['nome_do_arquivo']
    sys.stdout.write(
        f'Arquivo {deq} removido com sucesso\n'
    )


def file_metadata(instance, position):
    try:
        search = instance.search(position)
        return sys.stdout.write(str(search))
    except IndexError:
        sys.stderr.write('Posição inválida')
