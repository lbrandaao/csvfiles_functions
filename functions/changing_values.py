'''
Labels:
file = file that will be changed
new_file = file that will be created
perc = percentage that the values will increase or decrease
rows = list with the index of the rows that will be change
columns = list with the index of the columns that will be change 
sep = file's separator
orencoding = file's original encoding
newencoding = new_file's encoding
'''
#Need to add parameter to choose to increase or decrease values.




def changing_values(file, new_file, perc, rows, columns, sep = ',', orencoding = 'utf-8', newencoding = 'utf-8'):
    orfile = open(file, 'r', encoding = orencoding)
    newfile = open(new_file, 'w', encoding = newencoding)
    
    row = 0
    for line in orfile:
        if row in rows:
            sep_pos = 0
            sep_list = []
            for charac in line:           
                if charac == sep:
                    sep_list.append(sep_pos)
                sep_pos += 1
            
            fcolumn = len(sep_list)
            attributes = []
            for index_column in range(0, fcolumn + 1):              
                if index_column == 0:
                    attribute = line[:sep_list[index_column]]
                elif index_column == fcolumn:
                    attribute = line[sep_list[index_column - 1] + 1:]
                else:
                    attribute = line[sep_list[index_column - 1] + 1:sep_list[index_column]]
                attributes.append(attribute)
                
            new_line = ''
            for column in range(0, fcolumn + 1):               
                if column in columns:
                    new_value = int(attributes[column]) * (1 + (perc/100))
                    if column == fcolumn:
                        new_line += str(f'{new_value:.2f}') + '\n'
                    else:
                        new_line += str(f'{new_value:.2f}{sep}')
                
                else:
                    if column == fcolumn:
                        new_line += attributes[column]
                    else:
                        new_line += attributes[column] + sep
        
        else:
            new_line = line
        newfile.write(new_line)
        row += 1

    orfile.close()
    newfile.close()