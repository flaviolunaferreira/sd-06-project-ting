from ting_file_management.file_process import process
from ting_file_management.queue import Queue


def get_occurances(word, instance):
    length_instance = len(instance)
    occurances = []
    for index in range(length_instance):
        item = instance.search(index)
        line_content = item.get("linhas_do_arquivo")
        for i, content in enumerate(line_content, 1):
            if word.lower() in content.lower():
                occurance = {"linha": i}
                occurances.append(occurance)

    return occurances


def get_occurances_content(word, instance):
    length_instance = len(instance)
    occurances = []
    for index in range(length_instance):
        item = instance.search(index)
        line_content = item.get("linhas_do_arquivo")
        for i, content in enumerate(line_content, 1):
            if word.lower() in content.lower():
                occurance = {"linha": i, "conteudo": content}
                occurances.append(occurance)

    return occurances


def exists_word(word, instance):
    length_instance = len(instance)
    search_word_results = {}
    occurances = get_occurances(word, instance)
    if not occurances:
        return []

    for index in range(length_instance):
        item = instance.search(index)
        search_word_results["palavra"] = word
        search_word_results["arquivo"] = item.get("nome_do_arquivo")
        search_word_results["ocorrencias"] = occurances
    return [search_word_results]


def search_by_word(word, instance):
    length_instance = len(instance)
    search_word_results = {}
    occurances_content = get_occurances_content(word, instance)
    if not occurances_content:
        return []

    for index in range(length_instance):
        item = instance.search(index)
        search_word_results["palavra"] = word
        search_word_results["arquivo"] = item.get("nome_do_arquivo")
        search_word_results["ocorrencias"] = occurances_content
    return [search_word_results]


if __name__ == "__main__":
    project = Queue()
    path = "statics/nome_pedro.txt"
    process(path, project)
    word_search = search_by_word("pedro", project)
    print(word_search)
    # word_occurances = get_word_occurances("de", project)
    # print(word_occurances)
