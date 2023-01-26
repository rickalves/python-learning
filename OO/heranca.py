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
    @classmethod
    def __dar_like(self):
        self._likes += 1

# Subclasses
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
    
# Testando a classes
vingadores = Filme('Vingadores - Ultimato','Ação, Fantasia, Aventura', '2019', '180min')

print('+++++++++++++++++++++++++++++++++++++++++++++')
print(f'Filme:{vingadores.titulo}\nAno:{vingadores.ano}\n'+
      f'Duração:{vingadores.duracao}\nGênero:{vingadores.genero}\nLikes:{vingadores.likes}')

mandalorian = Serie('The Mandalorian','Ação, Fantasia, Aventura', '2020', '2 temporadas')

print('+++++++++++++++++++++++++++++++++++++++++++++')
print(f'Série:{mandalorian.titulo}\nAno:{mandalorian.ano}\n'+
      f'Temporadas:{mandalorian.temporadas}\nGênero:{mandalorian.genero}\nLikes:{mandalorian.likes}')