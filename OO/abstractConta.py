from abc import ABCMeta, abstractclassmethod
class Conta(metaclass=ABCMeta):
    def __init__(self, numero):
        self._numero = numero
        self._saldo = 0
    
    def __str__(self) -> str:
        return f'<<< Conta:{self._numero}, Saldo:{self._saldo} >>>'

    def __eq__(self, obj: object) -> bool:
        return self._numero == obj._numero
    
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
    pass

# Testando classes

conta1 = ContaCorrente(3456)
conta2 = ContaPoupanca(6789)
# conta3 = ContaUniversitaria(6543) # Gera erro por não definir método abstrato

conta1.deposita(2000)
conta2.deposita(1000)

contas = [conta1, conta2] #lista de contas

for conta in contas:
    print(conta)

for conta in contas:
    conta.passaMes()

for conta in contas:
    print(conta)