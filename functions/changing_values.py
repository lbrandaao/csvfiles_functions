def changing_values(file, new_file, perc, rows, columns, increase = True, sep = ',', orencoding = 'utf-8', newencoding = 'utf-8'):
    orfile = open(file, 'r', encoding = orencoding)
    newfile = open(new_file, 'w', encoding = newencoding)
    
    row = 1
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
            n_columns = len(sep_pos) + 1
            for column in columns:
                if column == 1:
                    new_value = int(line[:sep_list[0]]) * (1 + (perc/100))
                elif column == n_columns:
                    new_value = int(line[sep_list[-1]:]) * (1 + (perc/100))
                else:
                    new_value = int(line[sep_list[column-1] + 1:sep_list[column]])
                new_values.append(new_value)
            
            count_column = 1
            n = 0
            for charac in line:
                if count_column in columns:
                    new_line += str(new_values[n])
                    n += 1
                else:
                    new_line += charac
                if charac == sep:
                    count_column += 1


                
            