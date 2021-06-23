def exists_word(word, instance):
    matches = []
    for index in range(len(instance)):
        file = instance.search(index)
        word_found = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for i, line in enumerate(file["linhas_do_arquivo"]):
            if word in line:
                word_found["ocorrencias"].append({
                    "linha": i + 1
                })
        if len(word_found["ocorrencias"]):
            matches.append(word_found)
    return matches


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
