import unicodedata

def conversor_csv(file, new_file, orsep, newsep, ordecsep = '.', spechar = True, orencoding = 'utf-8', newencoding = 'utf-8'):
    
    if orsep == ordecsep:
        return print('Impossible conversion. Columns and decimals separators are equals.')
    
    file_read = open(arquivo, 'r', encoding = orencoding)
    file_write = open(novo_arquivo, 'w', encoding = newencoding)

    if spechar == True and ordecsep == '.':
        reading = file_read.read()
        new_content = reading.replace(orsep, newsep)
        file_write.write(new_content)
    
    elif spechar == True:
        reading = file_read.read()
        new_content = reading.replace(ordecsep, '.').replace(orsep, newsep)
        file_write.write(new_content)

    elif ordecsep == '.':
        reading = file_read.read()
        new_content = reading.replace(orsep, newsep)
        nfd = unicodedata.normalize('NFD', new_content)
        equi_content = u"".join([c for c in nfd if not unicodedata.combining(c)])
        file_write.write(equi_content)

    else:



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''if caracesp == False and sepor == ',':
        for line in file_read:
            line = line.replace(sepor, sepnov)
            nfd = unicodedata.normalize('NFD', line)
            equi_line = u"".join([c for c in nfd if not unicodedata.combining(c)])
            file_write.write(equi_line)
    
    elif caracesp == False:
        for line in file_read:
            line = line.replace(',', '.').replace(sepor, sepnov)
            nfd = unicodedata.normalize('NFD', line)
            equi_line = u"".join([c for c in nfd if not unicodedata.combining(c)])
            file_write.write(equi_line)
    
    elif sepor == ',':
        for line in file_read:
            line = line.replace(sepor, sepnov)
            file_write.write(line)
    else:
        for line in file_read:
            line = line.replace(',', '.').replace(sepor, sepnov)
            file_write.write(line)'''

#Em alguns casos, dados numéricos decimais podem possuir ',' para indicar os algarismos decimais. Caso o separador das colunas também seja ',' é impossível diferir o indicador de casas decimais e o separador de coluna (sempre que o indicador e o separador forem a mesma string isso ocorre). Portanto, caso o separador original não seja ',', a função sempre irá substituir o indicador de casas decimais ',' por '.'.

#Necessário aprimorar para o caso de dados separados por '.' e números decimais com ','.
