from collections import defaultdict
import string

someText = "Em Python existem dois tipos de estruturas de dados: "\
    "as sequências que são objetos ordenados e finitos (strings, listas e tuplas) " \
    "e dicionários que são conjuntos de elementos de mapeamento indexados por chaves. As Chaves " \
    "que devem ser únicas 55"

someText = someText.lower()
print(someText)

# replace digits for space
for x in string.digits:
    someText = someText.replace(x, ' ')

# replace punctuation for space
for x in string.punctuation:
    someText = someText.replace(x, ' ')

# print(someText)

words = defaultdict(int)
for word in someText.split():
    wcount = words[word]
    words[word] = wcount + 1

for word, wcount in words.items():
    print(f'{word}:{wcount}')