from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    """Aqui irá sua implementação"""
    path_list = instance.return_data()
    result = list()
    for file in path_list:
        content = txt_importer(file)
        occurrences = list()
        for index, line in enumerate(content):
            if word.casefold() in line.casefold():
                occurrences.append({"linha": index + 1})
        if len(occurrences) != 0:
            result_file = {
                "palavra": word,
                "arquivo": file,
                "ocorrencias": occurrences
            }
            result.append(result_file)
    return result

def search_by_word(word, instance):
    """Aqui irá sua implementação"""
