import unicodedata

def conversor_csv(file, new_file, orsep, newsep, ordecsep = '.', spechar = True, orencoding = 'utf-8', newencoding = 'utf-8'):
    
    if orsep == ordecsep:
        return print('Impossible conversion. Columns and decimals separators are equals.')
    
    file_read = open(file, 'r', encoding = orencoding)
    file_write = open(new_file, 'w', encoding = newencoding)

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
        reading = file_read.read()
        new_content = reading.replace(ordecsep, '.').replace(orsep, newsep)
        nfd = unicodedata.normalize('NFD', new_content)
        equi_content = u"".join([c for c in nfd if not unicodedata.combining(c)])
        file_write.write(equi_content)

    file_write.close()
    file_read.close()


#Em alguns casos, dados numéricos decimais podem possuir ',' para indicar os algarismos decimais. Caso o separador das colunas também seja ',' é impossível diferir o indicador de casas decimais e o separador de coluna (sempre que o indicador e o separador forem a mesma string isso ocorre). Portanto, caso o separador original não seja ',', a função sempre irá substituir o indicador de casas decimais ',' por '.'.

#Necessário aprimorar para o caso de dados separados por strings diferentes de ',' ou ';' e com números decimais com ','.
