def exists_word(word, instance):
    obj = []

    for item in range(0, len(instance)):
        data = instance.search(item)
        results = {
            "palavra": word,
            "arquivo": data["nome_do_arquivo"],
            "ocorrencias": []
        }

        for index, sub_item in enumerate(data["linhas_do_arquivo"]):
            if word.lower() in sub_item.lower():
                results["ocorrencias"].append({
                    "linha": index + 1
                })

        if len(results["ocorrencias"]):
            obj.append(results)

    return obj


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
