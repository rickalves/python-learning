# Testando classes
from abstractConta import*

conta1 = ContaCorrente(3456, "Rick")
conta2 = ContaPoupanca(6789, "Lara")
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