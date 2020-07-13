import unicodedata

'''
Labels:
file = file that will be changed
new_file = file will be created
orsep =  original column separator
newsep = new column separator that you want
ordecsep = original decimals separator
spechar = specials characters
orencoding = file's original encoding
newencoding = new_file's encoding

In some cases, decimal numeric data may have the string ',' to indicate the decimal numbers. If the columns separator is also ',' it's impossible to differentiate 
the decimal indicator and the columns separator (actually it always happens when the indicator and the separator are the same string). Thus, if the original separator 
is not ',', the function'll always change the decimal indicator ',' for '.'.'''

def converter_csv(file, new_file, orsep, newsep, ordecsep = '.', spechar = True, orencoding = 'utf-8', newencoding = 'utf-8'):
    
    if orsep == ordecsep:
        return print('Impossible conversion. Columns and decimals separators are equals.')
    
    file_read = open(file, 'r', encoding = orencoding)
    file_write = open(new_file, 'w', encoding = newencoding)
    reading = file_read.read()
    
    if spechar == True and ordecsep == '.':
        new_content = reading.replace(orsep, newsep)
        file_write.write(new_content)
    
    elif spechar == True:
        new_content = reading.replace(ordecsep, '.').replace(orsep, newsep)
        file_write.write(new_content)

    elif ordecsep == '.':
        new_content = reading.replace(orsep, newsep)
        nfd = unicodedata.normalize('NFD', new_content)
        equi_content = u"".join([c for c in nfd if not unicodedata.combining(c)])
        file_write.write(equi_content)

    else:
        new_content = reading.replace(ordecsep, '.').replace(orsep, newsep)
        nfd = unicodedata.normalize('NFD', new_content)
        equi_content = u"".join([c for c in nfd if not unicodedata.combining(c)])
        file_write.write(equi_content)

    file_write.close()
    file_read.close()
