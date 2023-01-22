# Estudo de lista de item sem valores duplicados. Class 'set'
# SET não é uma lista sequencial
# SET é uma lista não ordenada de elementos

colecao = {11122233344, 22233344455, 33344455566}
print(colecao)
colecao.add(44455566677) #vai adicionar pois não existe ainda!
colecao.add(44455566677) # não vai adicionar pois já existe!
print(colecao)

for cpf in colecao:
     print(cpf)
