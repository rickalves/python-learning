from abc import ABCMeta, abstractclassmethod
class Conta(metaclass=ABCMeta):
    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome
        self._saldo = 0
    
    def __str__(self) -> str:
        return f'<<< Conta:{self.numero}, Saldo:{self._saldo}, Titular:{self.nome} >>>'

    def __eq__(self, obj: object) -> bool:
        return self.numero == obj.numero
    
    def deposita(self, valor):
        self._saldo += valor
    
    @abstractclassmethod
    def passaMes(self):
        pass

class ContaCorrente(Conta):
    def passaMes(self):
        self._saldo -= self._saldo * 0.04

class ContaPoupanca(Conta):
    def passaMes(self):
        self._saldo *= 1.05

class ContaUniversitaria(Conta):
     def passaMes(self):
        self._saldo *= 1.01
