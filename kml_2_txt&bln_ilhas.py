#!/usr/bin/env python
# coding: utf-8

#Converte um arquivo no formato kml em um arquivo txt #
                                                             
                                                             

arquivo = open('Itaoca_linha_de_costa_ilhas.kml', 'r')
list1 = arquivo.readlines()


#Contar numero de ilhas são representadas pelo arquivo
contador = 0    
for i in range(len(list1)):
    if '<tessellate>1</tessellate>' in list1[i]:
        contador = contador+1

contador = contador + 1


# definindo as variáveis para o loop
list2 = str()
aux = str()
# Loop para ler o numero de ilhas e deacordo com a ilha guardar seus pontos na variavel list2
for j in range(contador):
    
    for i in range(len(list1)):
    
        if '<name>Linha_de_costa_Ilhas' + str(j) + '</name>' in list1[i]:
            aux= list1[i+5]  
            
    list2 = list2 + aux
        

#Separando os valores por espaço
list3 = list2.split()

#Definindo a variável str1
str1 = []

#Escrevendo o arquivo com as lat long das ilhas num bloco continuo
arq2 = open('duas_colunas_contorno_ilhas.txt', 'w')

for i in range(len(list3)):
    
    str1 = list3.pop(0)
    list5=str1.split(',')
    long_lat = ('{:.14f}'.format(float(list5[0])) + ' '  + '{:.14f}'.format(float(list5[1])))
    arq2.writelines(long_lat)
    arq2.write('\n')
    
    
arq2.close()


# -----------------------------------------------------------------------------
#Transforma o arquivo txt criado anteriormente em formato bln                 #
#                                                                             #
#                                                                             #
#------------------------------------------------------------------------------


# -------------------------Leitura do arquivo txt ------------------------------------
arquivo = open('duas_colunas_contorno_ilhas.txt', 'r')
list1 = arquivo.readlines()

arquivo.close()


    
#Cria um arquivo no formato BLN 
escreve = open('contorno_ilhas.bln', 'w')

#Define o numero de ilhas a partir da primeira parte do script
n_ilhas = contador - 1 

#Insere o cabeçalho padrão do arquivo 
escreve.write('COAST\n')
escreve.write(str(n_ilhas) +'\n')


#Definição das variáveis utilizadas no loop 
list2 = list()
h=0

#Loop para carregar a lista List com as lat/long e sua escrita 

for i in range(0,(len(list1))):

           
        # Critério de parada quando atingir a última posição da list1
        
        if h == len(list1):
        
            h = h - 2
        
            v1 = list1[h]
            
            break
        # Se não atingir continue acessando o valor da lista e guarda na variável v1 
        # para comparação e escrita         
        else:
        
            v1 = list1[h]
    
        
        # List2 guarda todos os valores que serão selecionados pelo loop de 2 ordem
        
        list2.append(v1)
        
        # Loop de 2 ordem julga os valores que devem ser escritos no arquivo,
        # separa por bloco e conta a ultima posição
    
        for j in range(1,len(list1)):
            
            # Adiciona um posição para usar o próximo valor da lista para comparação 
            h = h + 1 
            
            
            # Julga se a lat/long são diferentes para continuar com o loop    
            if v1 != list1[h]:
        
                list2.append(list1[h])
              
            
            # Sendo o valor igual entre os valores selecionados termina o loop de 2 ordem
            if v1 == list1[h]:
            
            #Guarda os valores num bloco representado por um loop
                list2.append(list1[h])
                
               
                
                break
                
        
        # Guarda a posição do ultimo valor julgado para que o próximo loop continue
        # a partir da possição desse valor.
        h = h + 1

                
        
        #Escreve no inicio de cada bloco o numero de linhas                       
        escreve.write(str(len(list2)) + ' ' + '1' + ' ' + '1' + '\n')
    
        # Escreve os valores por bloco  num arquivo bln 
        for i in range (len(list2)):
            aux = list2[i]
            str1 = aux.replace('\n','')
            list3  = str1.split(' ')
            escreve.write(str(list3[0]+ ' ' + str(list3[1])) + ' ' + '0.0' + '\n')
        # Esvazia a list2 para o inicio do próximo bloco
        list2[:] = []    
              
  
escreve.close()

