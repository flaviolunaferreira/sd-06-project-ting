from ting_file_management.queue import Queue
from ting_file_management.file_process import process
import re
import sys


def exists_word(word, instance):
    output_analysis = []

    for index in range(len(instance)):
        file = instance.search(index)
        search_result = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
        }
        for index, line in enumerate(file["linhas_do_arquivo"], 1):
            ocurrences = []
            if re.search(word, line, re.IGNORECASE):
                ocurrences.append(
                    {
                        "linha": index,
                    }
                )
        if len(ocurrences) > 0:
            search_result["ocorrencias"] = ocurrences
            output_analysis.append(search_result)
        else:
            return []

        sys.stderr.write(str(output_analysis))
        return output_analysis


def search_by_word(word, instance):
    output_analysis = []

    for index in range(len(instance)):
        file = instance.search(index)
        search_result = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
        }
        for index, line in enumerate(file["linhas_do_arquivo"], 1):
            ocurrences = []
            if re.search(word, line, re.IGNORECASE):
                ocurrences.append(
                    {
                        "linha": index,
                        "conteudo": line,
                    }
                )
        if len(ocurrences) > 0:
            search_result["ocorrencias"] = ocurrences
            output_analysis.append(search_result)
        else:
            return []

        sys.stderr.write(str(output_analysis))
        return output_analysis


if __name__ == "__main__":
    project = Queue()
    process("statics/nome_pedro.txt", project)
    word = exists_word("Pedro", project)
