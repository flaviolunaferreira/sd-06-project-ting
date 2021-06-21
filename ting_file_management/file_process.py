import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    exist = instance.find(path_file)
    if (instance.__len__() == 0 or exist == -1):
        conteudo = txt_importer(path_file)
        qtyLinhas = len(conteudo)
        sys.stdout.write(f"'nome_do_arquivo': '{path_file}'")
        sys.stdout.write(f"'qtd_linhas': {qtyLinhas}")
        sys.stdout.write(f"'linhas_do_arquivo': {conteudo}")
        instance.enqueue(path_file)


def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")

    removido = instance.dequeue()
    return sys.stdout.write(f"Arquivo {removido} removido com sucesso\n")


def file_metadata(instance, position):
    if (position > instance.__len__() - 1 or position < 0):
        sys.stderr.write('Posição inválida')
