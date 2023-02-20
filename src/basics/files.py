#Leitura e Escrita de arquivos em python

arquivo = open('./src/basics/citys.txt', 'w')#criando o arquivo em modo de escrita (Write)
arquivo.write('Gotham\n')
arquivo.write('New York\n')
arquivo.write('Sao Paulo\n')
arquivo.close()
arquivo = open('./src/basics/citys.txt', 'a')#abrindo o arquivo em modo de Append para escrever novamente no arquivo
arquivo.write('Rio de Janeiro\n')
arquivo.write('Guaraciaba do Norte\n')
arquivo.close()

# Abrindo arquivos em modo de leitura
arquivo_nomes = open('./src/basics/names.txt', 'r')#abrindo o arquivo em modo de leitura (Read)
nomes = []
for nome in arquivo_nomes:
    nome = nome.strip()
    nomes.append(nome)

arquivo_nomes.close()
# escrevendo os nomes
for nome in nomes:
    print(nome)

