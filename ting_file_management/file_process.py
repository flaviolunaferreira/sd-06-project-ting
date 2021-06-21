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
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    item_removed = instance.dequeue()["nome_do_arquivo"]
    return sys.stdout.write(f"Arquivo {item_removed} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
