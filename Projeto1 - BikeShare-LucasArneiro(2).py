
# coding: utf-8

# In[1]:


'''
PROJECT 1: "Chicago BikeShare" from Artifical Intelligence for Trading – NanoDegree - Udacity.
@uthor: Lucas Arneiro Vieira
Date: February, 10/2019 to March, 10/2019
'''

import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])


# In[2]:


# TAREFA 1
input("Aperte Enter para continuar...")
# Imprime as primeiras 20 linhas usando um loop para identificar os dados.

print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras: \n")

for row in range(1, 21):
    print (data_list[row]) 
    '''Imprimir as 20 primeiras linhas da lista "data_list"'''

#------------------------------------------------------------
    # Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]


# In[3]:


# TAREFA 2
input("Aperte Enter para continuar...")
# Imprime o gênero das primeiras 20 linhas.'''

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras: \n")

for i in range(21):
    print(data_list[i][6]) # Varre-se as linhas da coluna 6 (Gênero)


# In[4]:


# TAREFA 3
input("Aperte Enter para continuar...")
# Função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem.

def column_to_list(data, index):
    column_list = []
    for data in range(len(data_list)): 
        column_list.append(data_list[data][index])
    
    return column_list

    '''
    Função column_to_list
    -Argumentos:
       data = len(data_list) = linhas da matriz.
       index = posição da coluna da matriz.
       index = -2 # Posião fixa da coluna "Gender", pode ser a posição 6.
    -Retorna:
        Gera a coluna de qualquer elemento da lista "data_list"
    '''

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras: \n")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------


# In[9]:


# TAREFA 4
input("Aperte Enter para continuar...")
# Conte cada gênero: Iniciam-se zeradas, de modo a evitar erros 

male = 0
female = 0

for contagem in column_to_list(data_list, -2):

#Considerendo todos os elementos, linhas, da coluna 'Gender', ou -2, ou 6.
#contagem = Variavel pivô, varrendo o laço "for" 

    if (contagem == 'Male'):
            male += 1
    elif (contagem == 'Female'):
            female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos: \n")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------


# In[30]:


# TAREFA 5
input("Aperte Enter para continuar...")
# Função para contar os gêneros. Retorna uma lista.

def count_gender(data_list):
    male = 0
    female = 0
    male = column_to_list(len(data_list), -2).count('Male') 
    female = column_to_list(len(data_list), -2).count('Female')
    
    return [male, female]

'''
Função count_gender para contar o numero presente de cada Genero
-Argumentos:
   counter = Variavel pivô, varrendo o laço "for"
   male = Valor do numero de "Male".
   female = Valor do numero de "Female"
-Retorna:
    Número de vezes que um termo repete dentro da lista
'''

print("\nTAREFA 5: Imprimindo o resultado de count_gender: \n")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------


# In[32]:


# TAREFA 6
input("Aperte Enter para continuar...")

def most_popular_gender(data_list):
    answer = ""
    
    [count_male, count_female] = count_gender(data_list) 
    '''Chama a função que já faz a contagem de gêneros, armazenar os resultados em duas variáveis e utilizá-las em seu código.'''
    
    if count_male > count_female:
        answer = "Male"
    elif count_female > count_male:
        answer = "Female"
    else:
        answer = "Equal"
        
    return answer

'''
Função most_popular_gender: Determina o gênero mais popular, que aparece com maior frequência, na coluna gender.
-Argumentos:
   count_male = Variavel chamada, responsável por receber a quantidade de "Male" na count_gender
   count_female = Variavel chamada, responsável por receber a quantidade de "Female" na count_gender
   answer = Resposta final
-Retorna:
    Elemento que aparece com maior frequência na coluna gender.
'''

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------


# In[33]:


'''Criando gráfico para exibir valores de Gender, Male e Female, neste caso!'''
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)


# In[34]:


# TAREFA 7
input("Aperte Enter para continuar...")
    
# ================================== Gráfico similar ao de cima para user_types.========================================='''

# 1ª) CRIAR UMA LISTA COM "user_types": 

def usertypes_lista(line, coluna):
    user_list = []
    coluna = -3 
    
    for line in range(len(data_list)): 
        user_list.append(data_list[line][coluna])
    
    return user_list

    '''
    Função para lista dos "user_types 
    -Argumentos:    
       user_list = lista vazia de usuários.
       coluna = posição da coluna "user_types"
       Laço "for" varre as linhas na coluna[-3 ou 5] e adiciona em "user_list" com .append.
    -Retorna:
        A lista "user_list"
    '''

print(usertypes_lista(data_list, -3)[:20]) 
'''Teste de verificação, exibindo os primeiros 20 primeiros valores.'''


# 2ª) CRIAR UMA FUNÇÃO COM "user_types", para contar o número de "Customers" e Subscribers: 

def count_types(data_list):
    custom = 0
    subsc = 0
    custom = usertypes_lista(len(data_list), -3).count('Customer') 
    subsc = usertypes_lista(len(data_list), -3).count('Subscriber') 
    
    return [custom, subsc]

'''
    Função para lista dos "count_types
    -Argumentos:
       Utiliza-se .count para contar o número de vezes que um termo repete dentro da lista.
       custom = numero de consumidores
       subsc = numero de inscritos
    -Retorna:
         Numero de consumidores e inscritos
    '''

print("\n", count_types(data_list))


# 3ª) CRIAR UM GRÁFICO COM "user_types": 

print("\nTAREFA 7: Verifique o gráfico! \n")
types_list = usertypes_lista(data_list, -3)
tipo = ["Customer", "Subscriber"]
quantidade = count_types(data_list)
y_pos = list(range(len(tipo)))
plt.bar(y_pos, quantidade)
plt.ylabel('Quantidade')
plt.xlabel('Usuário')
plt.xticks(y_pos, tipo)
plt.title('Quantidade por Usuários')
plt.show(block=True)


# In[35]:


# TAREFA 8
input("Aperte Enter para continuar...")

male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa? \n")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Considerando a lista da base de dados em 'chicado.csv', referente ao projeto Chicago BikeShare, temos que os dados  da coluna 'Gender', ou 'Gênero' não foi preenchida por todos os 1551506 usuários cadastrados. Com isso, a soma de Gêneros dos  sexo, Masculino e Feminino, não serão iguais ao número total de cadastros realizados."


print ("\n-Resposta: \n\n", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------


# In[37]:


# TAREFA 9
input("Aperte Enter para continuar...")

'''Ache a duração de viagem Mínima, Máxima, Média, e Mediana.'''

trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.
size = 0 # Arredondamento da metade do tamanho ou do número de elementos da lista: trip_duration_inteiros

trip_duration_inteiros = list(map(int, trip_duration_list)) #
'''CONVERTER E CRIAR UMA LISTA COM "trip_duration_inteiros".'''

trip_duration_inteiros.sort() 
'''Orgazinar a lista de forma crescente'''

min_trip = trip_duration_inteiros[0]
'''Considerando a lista em ordem crescente, pegamos o primeiro valor, sendo o menor valor'''
#print('\nDuracao minima da viagem = {} unidades de tempo'.format(min_trip))

max_trip = trip_duration_inteiros[len(trip_duration_inteiros) - 1]
'''Considerando a lista em ordem crescente, pegamos o ultimo valor, sendo o maior valor'''
#print('\nDuracao maxima da viagem = {} unidades de tempo'.format(max_trip))

mean_trip = round(sum(trip_duration_inteiros) / len(trip_duration_inteiros))                                      
'''Soma-se todos os elementos da lista e divide-se pelo numero totais de elementos. round() = arredonda valores'''
#print('\nDuracao media das viagens = {} unidades de tempo'.format(mean_trip))

size = round(len(trip_duration_inteiros)/2)
if (size % 2 == 0):
    median_trip = (trip_duration_inteiros[size + 1] + trip_duration_inteiros[size + 2])/2
else:
    median_trip = trip_duration_inteiros[size + 1]    
'''
Pegamos metade do tamanho da lista para identificar sua respectiva posição. 
Caso seja um numero par, temos o elemento como uma media de: A posição media + 1 + posição media + 2.
Caso seja impar, temos o elemento na utima posição + 1, respectivamente, ao valor médio de elementos da lista.
'''

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------


# In[38]:


# TAREFA 10
input("Aperte Enter para continuar...")
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?

start_stations = set(column_to_list(data_list, 3))
'''Elimina os repetidos da start_stations, usando set()'''

print("\nTAREFA 10: Imprimindo as start stations: \n")
print('\nNumero de elementos em "start_stations": ', len(start_stations))
print('\n', start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# ----------------------------------------------------- 


# In[39]:


# TAREFA 12
input("Aperte Enter para continuar...")
# Função para contar tipos de usuários, sem definir os tipos.'''
# De modo a usar essa função com outra categoria de dados.

print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"
    
def count_items(column_list):
    item_types = []
    count_items = []
    
    colum = int(input('\nDigite o indice da coluna desejada: ')) # Nosso caso para teste: -2 
    print('\n')
    for linhas in range(len(data_list)): 
        item_types.append(data_list[linhas][colum]) 
        
    # print(item_types[:20]) # Exibe os 20 primeiros elementos da lista criada, como teste de funcinamento
    
    types = set(item_types) # Elementos unicos da lista, ou seja, os tipos de usuarios na lista.
    print(item_types)
    
    
    for tipo in types:
        for roww in item_types:
            if (tipo == roww):
                counts += 1
    
    return item_types, count_items
'''
Função para lista dos "count_items". Conta número unicos de elementos cadastrados na lista
-Argumentos:    
   item_types = lista criada a partir da coluna desejada.
   types = lista com valores unicos da lista "item_types".
   counts = numero de elementos na lista
   .
-Retorna:
    Quantidade de elementos únicos e  
'''

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------


# In[ ]:


''' **********************************ATENÇÃO!!!!**********************************************************

DÚVIDAS: Por favor, gostaria de esclarece-las, na correção.

1- TAREFA 12: Não entendi muito bem a sequência do "for" para pegar os tipos de usuários...não seria somente "len()" necessário?

***********************************************************************************************************'''

