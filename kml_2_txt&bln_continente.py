#!/usr/bin/env python
# coding: utf-8

#--------------------------------------------------#
# Converte um arquivo kml em txt                   #
#--------------------------------------------------#

arquivo = open('Itaoca_linha_de_costa.kml', 'r')
list1 = arquivo.readlines()


for i in range(len(list1)):
    
    if '<coordinates>' in list1[i]:
        str1 = list1[i+1]
        

# Separa uma string única contida no list2 com os dados lat long e zero separados por espaços em branco em um arquivo list3
# numa lista onde cada linha contem Lat long e zeros.
#list3 = list2.split()

# Remove a primeira linha da lista e guarda na variável str1 e transforma numa string
#str1 = list3.pop()

# Separa os dados da variavel tipo string str1 separados por virgula numa variavel tipo lista em list5
#list5=str1.split(',')

# Transforma os dados tipo string em dados tipo float e guarda o valor de longitude e latitude
#long, lat = float(list5[0]) , float(list5[1]) Obs Nao usei essa linha ainda

#Testando o procedimento anterior num laço

list3 = str1.split()

#aux = list2.split() 

str2 = []

arq2 = open('contornoTerra2colunas.txt','w')

for i in range(len(list3)):
    
    str2 = list3.pop(0)
    list5=str2.split(',')
    long_lat = ('{:.14f}'.format(float(list5[0])) + ' '  + '{:.14f}'.format(float(list5[1])))
    arq2.writelines(long_lat)
    arq2.write('\n')
    
    
arq2.close()


# ------------------------------------------------------------------ #
# Converte o arquivo txt em bln
#--------------------------------------------------------------------#
                                   


#Ler as linhas do arquivo com as lat e long e guarda numa lista.
arquivo = open('contornoTerra2colunas.txt', 'r')
list1 = arquivo.readlines()

arquivo.close()
   
    
# Cria um arquivo no formato BLN
 
escreve = open('contorno_costa.bln', 'w')
escreve.write('COAST\n')
escreve.write('1\n')
escreve.write(str(len(list1)) + ' ' + '1' + ' ' + '1\n')

for i in range(len(list1)):
    aux = list1[i]
    str1 = aux.replace('\n','')
    list2  = str1.split(' ')
    escreve.write(str(list2[0]+ ' ' + str(list2[1])) + ' ' + '0.0' + '\n')
  
escreve.close()




