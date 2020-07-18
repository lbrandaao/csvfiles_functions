 def changing_values(file, new_file, perc, rows, columns, sep = ',', orencoding = 'utf-8', newencoding = 'utf-8'):
     orfile = open(file, 'r', encoding = orencoding)
     newfile = open(new_file, 'w', encoding = newencoding)

     rows_count = 2
     for line in orfile:
         columns_count = 1
         if rows_count in rows:
            for word in line:
                if word == sep:



