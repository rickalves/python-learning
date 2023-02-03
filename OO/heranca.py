# Definindo Classe mãe
class Producao:
    def __init__(self, titulo, genero, ano):
        self._titulo = titulo
        self._genero = genero
        self._ano = ano
        self._likes = 0
    
    # getters e setters
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self, genero):
        self._genero = genero
    
    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, ano):
        self._ano = ano
    
    @property
    def likes(self):
        return self._likes
    
    # outros métodos
    def dar_like(self):
        self._likes += 1
    
    def __str__(self):
        return f'Filme:{self._titulo}\nAno:{self._ano}\nGênero:{self._genero}\nLikes:{self._likes}'

# Subclasses ++++++++++++++++++++++++++++++++++++++++++++++++
class Filme(Producao):
    def __init__(self, titulo, genero, ano, duracao):
        super().__init__(titulo, genero, ano)
        self._duracao = duracao

    @property
    def duracao(self):
        return self._duracao
    
    @duracao.setter
    def duracao(self, duracao):
        self._duracao = duracao
    
    def __str__(self):
       return f'Filme:{self._titulo}\nAno:{self._ano}\nDuração:{self._duracao}\nGênero:{self._genero}\nLikes:{self._likes}'
      
class Serie(Producao):
    def __init__(self, titulo, genero, ano, temporadas):
        super().__init__(titulo, genero, ano)
        self._temporadas = temporadas

    @property
    def temporadas(self):
        return self._temporadas

    @temporadas.setter
    def temporadas(self, temporadas):
        self._temporadas = temporadas 

    def __str__(self):
       return f'Série:{self._titulo}\nAno:{self._ano}\nTemporadas:{self._temporadas}\nGênero:{self._genero}\nLikes:{self._likes}'

    
# Testando a classes
vingadores = Filme('Vingadores - Ultimato','Ação, Fantasia, Aventura', '2019', '180 min')
vingadores.dar_like()
print(vingadores)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
mandalorian = Serie('The Mandalorian','Ação, Fantasia, Aventura', '2020', '2 temporadas')
print(mandalorian)

