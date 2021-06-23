import sys
from ting_file_management.file_management import txt_importer

path_list = []


def process(path_file, instance):
    if instance.__len__() == 0:
        file = txt_importer(path_file)
        path_list.append(path_file)

        file_name = f"'nome_do_arquivo': '{path_file}'"
        qt_lines = f"'qtd_linhas': {len(file)}"
        lines = f"'linhas_do_arquivo': {file}"

        sys.stdout.write(f'{file_name}')
        sys.stdout.write(f'{qt_lines}')
        sys.stdout.write(f'{lines}')

        instance.enqueue(path_file)
    else:
        pass


def remove(instance):
    if instance.__len__() == 0:
        sys.stdout.write('Não há elementos\n')
    else:
        instance.dequeue()
        path_name = path_list[0]
        path_list.remove(path_name)
        sys.stdout.write(f'Arquivo {path_name} removido com sucesso\n')


def file_metadata(instance, position):
    if position < 0 or position > len(path_list):
        sys.stderr.write('Posição inválida\n')
    else:
        sys.stdout.write(instance.search(position))
