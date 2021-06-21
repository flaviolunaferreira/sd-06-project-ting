from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    path_list = instance.return_data()
    result = list()
    for file in path_list:
        content_file = txt_importer(file)
        occcurrences = list()
        for index, line in enumerate(content_file):
            if word.casefold() in line.casefold():
                occcurrences.append({"linha": index + 1})
        if len(occcurrences) != 0:
            file_result = {
                "palavra": word,
                "arquivo": file,
                "ocorrencias": occcurrences
            }
            result.append(file_result)
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
