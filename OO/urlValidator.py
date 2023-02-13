'''
Verifica se a base da URL está em um padrão correto

Exemplos de URLs válidas
    bytebank.com/cambio
    bytebank.com.br/cambio
    www.bytebank.com/cambio
    www.bytebank.com.br/cambio
    http://www.bytebank.com/cambio
    http://www.bytebank.com.br/cambio
    https://www.bytebank.com/cambio
    https://www.bytebank.com.br/cambio

Exemplos de URL inválidas
    bytebank/cambio
    http://bytebank/cambio
    http://bytebank.us/cambio
    http//bytebank.com/cambio

'''
import re

padrao = re.compile("(http(s)?://)?(www.)?[a-z]+.com(.br)?(/)?([a-z]+)?")
url = "https://www.bytebank.com.br/cambio"
busca = padrao.match(url)
if busca:        
    print(busca)
else:
    raise ValueError("Padrão não Encontrado!")
    
