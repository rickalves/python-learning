from datetime import datetime
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Criando a conta do titular: {}".format(titular))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print("\n------Extrato da Conta-------")
        print("Número:{}".format(self.__numero))
        print("Titular:{}".format(self.__titular))
        print("Saldo:{}".format(self.__saldo))
        data = datetime.now()
        print("Data:{}".format(data.strftime('%d/%m/%Y %H:%M')))
    
    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor
    
    def alterarLimite(self, valor):
        self.limite = valor
    
    def transferir(self, conta, valor):
        conta.depositar(valor)
        self.__saldo -= valor

# getters e setters
    def get_titular(self):
        return self.__titular

    def get_numero(self):
        return self.__numero

    def get_saldo(self):
        return self.__saldo
    
    def get_limite(self):
        return self.__limite

    def set_titular(self, valor):
        self.__titular = valor

    def set_limite(self, valor):
        self.__limite = valor