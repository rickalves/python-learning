from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, valor):
        self._salario = valor

    def decrescimo_salario(self):
        if self._salario >= 100000:
            decrescimo = self._salario * 0.1
            self._salario -= decrescimo

    def sobrenome(self):
        nome = self._nome.strip()
        nome = nome.split(' ')
        sobrenome = nome[-1]
        return sobrenome

    def idade(self):
        ano_atual = date.today().year
        ano_idade = str(self._data_nascimento).split("/")
        return ano_atual - int(ano_idade[-1])

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception("Salário não se enquadra no bônus!")
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'