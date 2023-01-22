# Estudo de listas homogêneas mutáveis em Python class 'list'

valores = [1,2,3,4,5,6,7,8,9,10]
lista = range(0, 20)
print(type(valores))
print(max(valores))#valor máximo
print(max(lista))#valor máximo
print(min(valores))#Valor mínimo
print(valores[4])#valor específico
print(len(valores))#tamanho da lista
print(valores[2:6])#fatiamento de lista
print(2 in valores)#retorna True para item buscado presente na lista
print(5 not in valores) #retorna True para item buscado não presente na lista
print(valores.count(1)) #retorna o numero de ocorrencias de um determinado valor.
print(valores.index(5)) #retorna o indice de um determinado valor.

# Funções de lista
valores.append(20)#adiciona valor ao final da lista
print(valores)
valores.pop()#remove item do final da lista.
print(valores)
valores.remove(9)#remove item específico da lista passado por parametro.
print(valores)
valores.reverse()#inverte a ordem dos items da lista
print(valores)
# valores.clear()##remove todos os itens da lista
# print(valores)
