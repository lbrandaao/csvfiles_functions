import unicodedata
import pandas as pd

def conversor_csv(arquivo, novo_arquivo, modo):
    file_read = open(arquivo, 'r')
    file_write = open(novo_arquivo, 'w')
    
    '''A finalidade do modo 'pandas' é converter um arquivo csv com separador ';' e com normalização NFC, para o separador ',' e remover acentos. Assim o pandas é capaz de ler.'''
    if modo == 'pandas':
        for line in file_read:
            nfkd = unicodedata.normalize('NFKD', line) #Normalização da linha na forma NKFD.
            semacento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
            new_line = semacento.replace(',','.') #.replace(';', ',') caso não use o parâmetro (sep=','). 
            file_write.write(new_line)