from .file_management import txt_importer
import sys


def process(path_file, instance):
    file_content = txt_importer(path_file)

    output_message = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": file_content,
    }
    instance.enqueue(output_message)

    sys.stdout.write(str(output_message))


def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")
    removed_file = instance.dequeue()
    print(removed_file)
    return sys.stdout.write(
        f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso\n"
    )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
