from ting_file_management.file_process import process
from ting_file_management.queue import Queue
import re


def exists_word(word, instance):
    data = instance.search(0)
    match = re.search(word, data['linhas_do_arquivo'][0])
    result = list()
    result.append({
        "palavra": word,
        "arquivo": data['nome_do_arquivo'],
        "ocorrencias": [{
            "linha": data['qtd_linhas']
        }]
    })
    if match:
        return result
    else:
        return []


def search_by_word(word, instance):
    data = instance.search(0)
    match = re.search(word, data['linhas_do_arquivo'][0], re.IGNORECASE)
    result = list()
    result.append({
        "palavra": word,
        "arquivo": data['nome_do_arquivo'],
        "ocorrencias": [{
            "linha": data['qtd_linhas'],
            "conteudo": data['linhas_do_arquivo'][0]
        }]
    })
    if match:
        return result
    else:
        return []


project = Queue()
process("statics/nome_pedro.txt", project)
print(search_by_word("pedro", project))
