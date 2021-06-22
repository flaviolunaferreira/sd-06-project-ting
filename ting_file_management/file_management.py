import sys


def txt_importer(path_file):
    try:
        if path_file.endswith('.txt'):
            with open(path_file, mode="r") as txt_file:
                output = txt_file.readlines()
                format_output = [line.strip('\n') for line in output]
                return format_output
        else:
            return print("Formato inválido", file=sys.stderr)
    except OSError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)


if __name__ == "__main__":
    txt = txt_importer("/home/isabella/sd-06-projects/sd-06-project-ting/statics/arquivo_teste.txt")
