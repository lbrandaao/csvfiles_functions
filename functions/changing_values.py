def changing_values(file, new_file, perc, rows, columns, increase = True, sep = ',', orencoding = 'utf-8', newencoding = 'utf-8'):
    orfile = open(file, 'r', encoding = orencoding)
    newfile = open(new_file, 'w', encoding = newencoding)
    
    row = 1
    for line in orfile:
        if row in rows:
            sep_pos = 0
            sep_list = []
            for charac in line:
                if charac == sep:
                    sep_list.append(sep_pos)
                sep_pos += 1
            new_line = ''
            for column in columns:
                if column == 1:
                    new_value = int(line[:sep_pos[0]]) * (1 + (perc/100))
                    new_line += str(new_value) + sep