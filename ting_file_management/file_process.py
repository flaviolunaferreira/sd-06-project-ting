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
    try:
        instance.dequeue()
        sys.stdout.write(f'{instance}\n')
    except ValueError:
        sys.stderr.write('Não há elementos')


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        return sys.stdout.write(str(file))
    except IndexError:
        return sys.stderr.write('Posição inválida')
