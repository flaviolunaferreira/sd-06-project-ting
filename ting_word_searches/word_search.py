from ting_file_management.file_process import process
from ting_file_management.queue import Queue
import re


def exists_word(word, instance):
    data = instance.return_data()[0]
    match = re.search(word, data)
    result = list()
    result.append({
        "palavra": word,
        # arquivo hardcoded, como encontrar o path_file?
        "arquivo": "statics/nome_pedro.txt",
        # arquivo hardcoded, como encontrar o número de linhas?
        "ocorrencias": [{"linha": 1}]
    })
    if match:
        return result
    else:
        return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


project = Queue()
process("statics/nome_pedro.txt", project)
print(exists_word("maria", project))
