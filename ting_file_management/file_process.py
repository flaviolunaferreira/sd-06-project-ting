from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file_length = instance.__len__()
    if (file_length == 0):
        file_read = txt_importer(path_file)
        qtd_lines = len(file_read)
        instance.enqueue(path_file)
        format_info = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": qtd_lines,
            "linhas_do_arquivo": file_read
            }
        sys.stdout.write(f"{format_info}")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """https://docs.python.org/pt-br/3/library/shutil.html"""
