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
        return f'\nFilme:{self._titulo}\nAno:{self._ano}\nGênero:{self._genero}\nLikes:{self._likes}'

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
       return f'\nFilme:{self._titulo}\nAno:{self._ano}\nDuração:{self._duracao}\nGênero:{self._genero}\nLikes:{self._likes}'
      
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
       return f'\nSérie:{self._titulo}\nAno:{self._ano}\nTemporadas:{self._temporadas}\nGênero:{self._genero}\nLikes:{self._likes}'

#Criando a classe playlist++++++++++++++++++++++++++++
class Playlist:
    def __init__(self, nome, producoes):
        self._nome = nome
        self._producoes = producoes
    
    def __getitem__(self, item):
        return self._producoes[item]

    def __len__(self):
        return len(self._producoes)

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome



# Testando a classes
vingadores = Filme('Vingadores - Ultimato','Ação, Fantasia, Aventura', '2019', '180 min')
johnWick4 = Filme('John Wick 4 - Babayega','Ação, Aventura', '2023', '180 min')
vingadores.dar_like()
johnWick4.dar_like()

mandalorian = Serie('The Mandalorian','Ação, Fantasia, Aventura', '2020', '2 temporadas')
starwars_clone_wars = Serie('Star Wars - Clone Wars','Ação, Fantasia, Aventura', '2018', '5 temporadas')

producoes = [vingadores, johnWick4, mandalorian, starwars_clone_wars]

playlist = Playlist("Filmes e Series", producoes)

for producao in playlist:
    print(producao)

print(f'O tamanho da playlist é: {len(playlist)}')


