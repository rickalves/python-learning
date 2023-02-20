from collections import Counter
from decimal import*

someText = """
Python é uma linguagem de programação de alto nível, ou seja, com sintaxe mais simplificada e 
próxima da linguagem humana, utilizada nas mais diversas aplicações, como desktop, web, servidores
 e ciência de dados. Saiba mais sobre ela, sua origem e principais vantagens neste guia para iniciantes.

"""
# show the letters count
lettersCounter = Counter(someText)
print("-------Letters Count----------")
for letter, lcount in lettersCounter.items():
    if(letter == '\n'):
        print(f"'\\n':{lcount}")
    else:
        print(f"'{letter}':{lcount}")


# show the 10 most common letters
lTotal = sum(lettersCounter.values())
proportion = [(letter, round(freq/lTotal, 2)) for letter, freq in lettersCounter.items()]
proportion = Counter(dict(proportion))

# for l, f in proportion.items():
#     print(f"'{l}'->{round(f*100, 2)}%")
tenMost = proportion.most_common(10)

print("------Most common Letters-------")
for l, f in tenMost:
    print(f"'{l}'->{round(f*100, 2)}%")



