import unicodedata
import pandas as pd

def conversor_excel(arquivo, novo_arquivo, modo):
    if modo == 'pycharm':
        file_read = open(f'C:\\Users\\leona\\PycharmProjects\\CursoDados\\arquivos_excel\\{arquivo}', 'r')
        file_write = open(f'C:\\Users\\leona\\PycharmProjects\\CursoDados\\arquivos_excel\\{novo_arquivo}', 'w')
        for line in file_read:
            nfkd = unicodedata.normalize('NFKD', line)
            semacento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
            new_line = semacento.replace(',','.').replace(';', ',')
            file_write.write(new_line)