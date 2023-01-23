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
        print(str("Saldo:R$:%.2f" % self.__saldo).replace('.', ','))
        print(str("Limite disponível:R$:%.2f"%self.__limite).replace('.', ','))
        print(str("Limite Total:R$:%.2f"%(self.__limite+self.__saldo)).replace('.', ','))
        data = datetime.now()
        print("Data/Hora:{}".format(data.strftime('%d/%m/%Y - %H:%M')))

    def __limite_disponivel(self, valor):
        limite_disponivel = self.__saldo + self.__limite
        return valor <= limite_disponivel

    def __atualiza_saldo_limite(self, valor):
        if (self.__saldo >= valor):
            self.__saldo -= valor
        else:
            if(self.__saldo != 0):
                self.__limite -= valor - self.__saldo
                self.__saldo = 0
            else:
                self.__limite -= valor 

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if(self.__limite_disponivel(valor)):
            self.__atualiza_saldo_limite(valor)
        else:
            print("\nFalha ao sacar:Limite indisponível!")
        
    
    def alterarLimite(self, valor):
        self.limite = valor
    
    def transferir(self, conta, valor):
        if(self.__limite_disponivel(valor)):
            conta.depositar(valor)
            self.__atualiza_saldo_limite(valor) 
        else:
            print("\nFalha ao transferir:Limite indisponível!")
       
    
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