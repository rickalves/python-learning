#resolver problema da importação
from main.oo import abstractConta

conta_rick = abstractConta.ContaCorrente(3453, "Rick")
conta_lara = abstractConta.ContaPoupanca(7890, "Lara")
conta_john = abstractConta.ContaUniversitaria(4456, "Mary")

contas = [conta_john, conta_lara, conta_rick]

for conta in contas:
    print(conta)