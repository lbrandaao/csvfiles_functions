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
    
    else:
        if sepor == ','
            for line in file_read:
                line = line.replace(sepor, sepnov)
                file_write.write(line)
        else:
            for line in file_read:
                line = line.replace(',', '.').replace(sepor, sepnov)
                file_write.write(line)