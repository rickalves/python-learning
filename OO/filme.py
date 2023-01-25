class Filme:
    def __init__(self, titulo, duracao, genero, ano):
        self.__titulo = titulo
        self.__duracao = duracao
        self.__genero = genero
        self.__ano = ano
        self.__likes = 0
    # getters e setters
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
    
    @property
    def duracao(self):
        return self.__duracao
    
    @duracao.setter
    def duracao(self, duracao):
        self.__duracao = duracao

    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, genero):
        self.__genero = genero
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        self.__ano = ano
    
    @property
    def likes(self):
        return self.__likes
    
    # outros métodos
    def __dar_like(self):
        self.__likes += 1

    
# Testando a classe
vingadores = Filme('Vingadores - Ultimato', '180min', 'Ação, Fantasia, Aventura', '2019')
print(f'Filme:{vingadores.titulo}\nAno:{vingadores.ano}\n'+
      f'Duração:{vingadores.duracao}\nGênero:{vingadores.genero}\nLikes:{vingadores.likes}')