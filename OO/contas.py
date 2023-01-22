#Utilizando classe conta
from conta import Conta

conta1 = Conta(3435, "Rick", 500.0, 1000.0)
conta2 = Conta(6786, "Lara", 100.0, 1500.0)

conta1.depositar(100.0)
conta2.depositar(200.0)

conta1.extrato()
conta2.extrato()

# mosntrando o limite da conta formatado
limite = "O limite da conta {} é: R$ %.2f".format(conta1.get_numero())%conta1.get_limite()
print(limite.replace('.', ','))