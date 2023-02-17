#Leitura e Escrita de arquivos em python

arquivo = open('./basics/citys.txt', 'w')#criando o arquivo em modo de escrita (Write)
arquivo.write('Gotham\n')
arquivo.write('New York\n')
arquivo.write('Sao Paulo\n')
arquivo.close()
arquivo = open('citys.txt', 'a')#abrindo o arquivo em modo de Append para escrever novamente no arquivo
arquivo.write('Rio de Janeiro\n')
arquivo.close()

# Abrindo arquivos em modo de leitura
arquivo_nomes = open('./basics/names.txt', 'r')#abrindo o arquivo em modo de leitura (Read)
nomes = []
for nome in arquivo_nomes:
    nome = nome.strip()
    nomes.append(nome)
arquivo_nomes.close()
print(nomes[len(nomes)-1])
