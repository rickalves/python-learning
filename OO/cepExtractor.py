endereco = "Av. Capitão  Ferreira, 722, 62380-000, Guaraciaba do Norte-CE"

# biblioteca de Regular Expression RE do python
import re

padrao = re.compile("[0-9]{5}-?[0-9]{3}")
busca = padrao.search(endereco)
print(busca.group())