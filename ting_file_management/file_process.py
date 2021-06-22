import sys
# from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    fileObject = txt_importer(path_file)
    fileName = path_file.split("/")[1]
    # print(fileObject)
    # print(fileName)
    processedFile = {
        "nome_do_arquivo": fileName,
        "qtd_linhas": len(fileObject),
        "linhas_do_arquivo": fileObject,
    }

    if len(instance.queue) == 0:
        instance.enqueue(processedFile)
        sys.stdout.write(f"'nome_do_arquivo': '{path_file}'")
        sys.stdout.write(f"'qtd_linhas': {str(len(fileObject))}")
        sys.stdout.write(f"'linhas_do_arquivo': {fileObject}")
    else:
        for file in instance.queue:
            # print(fileName != file["nome_do_arquivo"])
            if fileName != file["nome_do_arquivo"]:
                instance.enqueue(processedFile)
                sys.stdout.write(f"'nome_do_arquivo': '{path_file}'")
                sys.stdout.write(f"'qtd_linhas': {str(len(fileObject))}")
                sys.stdout.write(f"'linhas_do_arquivo': {fileObject}")

    # processedFile = {
    #     "nome_do_arquivo": fileName,
    #     "qtd_linhas": len(fileObject),
    #     "linhas_do_arquivo": fileObject
    # }

    # print(processedFile)
    # instance.enqueue(processedFile)
    # sys.stdout(processedFile)
    # print(instance.queue)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# project = Queue()
# process("statics/arquivo_teste.txt", project)
# process("statics/arquivo_teste.txt", project)
