from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if any(
        queue["nome_do_arquivo"] == path_file for queue in instance.get_all()
    ):
        return "Queue error"

    lines = txt_importer(path_file)
    len_lines = len(lines)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len_lines,
        "linhas_do_arquivo": lines
    }
    instance.enqueue(result)
    return print(result, file=sys.stdout)


def remove(instance):
    if (len(instance.get_all()) == 0):
        return print("Não há elementos", file=sys.stdout)
    removed_item = instance.get_all()[0]['nome_do_arquivo']
    instance.dequeue()
    return print(
        f"Arquivo {removed_item} removido com sucesso",
        file=sys.stdout
    )


def file_metadata(instance, position):
    if (position >= len(instance)):
        return print("Posição inválida", file=sys.stderr)
    return print(instance.search(position), file=sys.stdout)
