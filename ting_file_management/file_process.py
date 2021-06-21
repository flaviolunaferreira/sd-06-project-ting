import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if not instance.find_file(path_file):
        file_content = txt_importer(path_file)
        instance.enqueue(path_file)
        lines = list()
        for line in file_content:
            lines.append(line)
        file_lines = len(lines)
        result = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": file_lines,
            "linhas_do_arquivo": file_content
        }

        sys.stdout.write(str(result))


def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")
    instance.dequeue()
    sys.stdout.write(
        "Arquivo statics/arquivo_teste.txt removido com sucesso\n"
    )


def file_metadata(instance, position):
    if position > instance.__len__() - 1:
        return sys.stderr.write("Posição inválida\n")
