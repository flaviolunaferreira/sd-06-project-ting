import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if instance.__len__() == 0:
        file = txt_importer(path_file)

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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
