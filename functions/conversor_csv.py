import unicodedata
import pandas as pd

def conversor_csv(arquivo, novo_arquivo, modo):
    file_read = open(arquivo, 'r')
    file_write = open(novo_arquivo, 'w')
    
    '''A finalidade do modo 'pandas' é converter um arquivo csv com separador ';', com normalização NFC e com números fracionários com ',' -> para separador ',', remover acentos e números fracionários com '.'. Assim o pandas é capaz de ler.'''
    if modo == 'pandas':
        for line in file_read:
            nfkd = unicodedata.normalize('NFKD', line) #Normalização da linha na forma NKFD.
            semacento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
            new_line = semacento.replace(',','.') #.replace(';', ',') caso não use o parâmetro (sep=',') em read_csv(). 
            file_write.write(new_line)