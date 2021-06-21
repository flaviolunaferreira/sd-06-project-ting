from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    n = instance.__len__()
    i = 0
    result = []
    while (i < n):
        file = instance.dequeue()
        conteudo = txt_importer(file)
        ocr = []
        for i in range(len(conteudo)):
            if word.lower() in conteudo[i].lower():
                ocr = [*ocr, {"linha": i+1}]
        if (len(ocr) > 0):
            newResult = {"palavra": word, "arquivo": file, "ocorrencias": ocr}
            result = [*result, newResult]
        i += 1

    return result


def search_by_word(word, instance):
    n = instance.__len__()
    i = 0
    result = []
    while (i < n):
        file = instance.dequeue()
        conteudo = txt_importer(file)
        ocr = []
        for i in range(len(conteudo)):
            if word.lower() in conteudo[i].lower():
                ocr = [*ocr, {"linha": i+1, "conteudo": conteudo[i]}]
        if (len(ocr) > 0):
            newResult = {"palavra": word, "arquivo": file, "ocorrencias": ocr}
            result = [*result, newResult]

        i += 1

    return result
