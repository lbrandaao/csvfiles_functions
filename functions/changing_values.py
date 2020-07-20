def changing_values(file, new_file, perc, rows, columns, increase = True, sep = ',', orencoding = 'utf-8', newencoding = 'utf-8'):
    orfile = open(file, 'r', encoding = orencoding)
    newfile = open(new_file, 'w', encoding = newencoding)
    
    row = 0
    for line in orfile:
        if row in rows:
            sep_pos = 0
            sep_list = []
            new_line = ''
            new_values = []
            for charac in line:
                if charac == sep:
                    sep_list.append(sep_pos)
                sep_pos += 1
            
            index_columns = len(sep_list)
            attributes = []
            column = 0
            while column <= index_columns:
                if column == 0:
                    attribute = line[:sep_list[column]]
                elif column == index_columns:
                    attribute = line[sep_list[column - 1]:]
                else:
                    attribute = line[sep_list[column - 1]:sep_list[column]]
                attributes.append(attribute)
                column += 1

            

            
            
            
            
            
            '''for column in columns:
                if column == 1:
                    new_value = int(line[:sep_list[0]]) * (1 + (perc/100))
                elif column == n_columns:
                    new_value = int(line[sep_list[-1]:]) * (1 + (perc/100))
                else:
                    new_value = int(line[sep_list[column-1] + 1:sep_list[column]])
                new_values.append(new_value)'''


                
            