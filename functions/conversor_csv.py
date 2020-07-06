import unicodedata
import pandas as pd

def conversor_csv(arquivo, novo_arquivo, sepor, sepnov, caracesp = False):
    file_read = open(arquivo, 'r')
    file_write = open(novo_arquivo, 'w')

    if caracesp == False and sepor == ',':
        for line in file_read:
            line = line.replace(sepor, sepnov)
            nfkd = unicodedata.normalize('NFKD', line)
            equi_line = u"".join([c for c in nfkd if not unicodedata.combining(c)])
            file_write.write(equi_line)
    
    elif caracesp == False:
        for line in file_read:
            line = line.replace(',', '.').replace(sepor, sepnov)
            nfkd = unicodedata.normalize('NFKD', line)
            equi_line = u"".join([c for c in nfkd if not unicodedata.combining(c)])
            file_write.write(equi_line)
    
    elif sepor == ',':
        for line in file_read:
            line = line.replace(sepor, sepnov)
            file_write.write(line)
    else:
        for line in file_read:
            line = line.replace(',', '.').replace(sepor, sepnov)
            file_write.write(line)

#Em alguns casos, dados numéricos decimais podem possuir ',' para indicar os algarismos decimais. Caso o separador das colunas também seja ',' é impossível diferir o indicador de casas decimais e o separador de coluna (sempre que o indicador e o separador forem a mesma string isso ocorre). Portanto, caso o separador original não seja ',', a função sempre irá substituir o indicador de casas decimais ',' por '.'.

#Necessário aprimorar para o caso de dados separados por '.' e números decimais com ','.