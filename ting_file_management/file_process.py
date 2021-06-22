from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    txt_data = txt_importer(path_file)
    output_file = {}

    output_file["nome_do_arquivo"] = path_file
    output_file["qtd_linhas"] = len(txt_data)
    output_file["linhas_do_arquivo"] = txt_data

    instance.enqueue(output_file)
    sys.stdout.write(str(output_file))


def remove(instance):
    if len(instance) != 0:
        item_removed = instance.dequeue()
        file_name = item_removed.get("nome_do_arquivo")
        sys.stdout.write(str(f"Arquivo {file_name} removido com sucesso\n"))
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


if __name__ == "__main__":
    project = Queue()
    path = "statics/arquivo_teste.txt"
    output = process(path, project)
    remove_file = remove(project)
