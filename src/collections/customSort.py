#resolver problema da importação
from src.oo import abstractConta as conta

conta_rick = conta.ContaCorrente(3453, "Rick")
conta_lara = conta.ContaPoupanca(7890, "Lara")
conta_john = conta.ContaUniversitaria(4456, "Mary")

contas = [conta_john, conta_lara, conta_rick]

for conta in contas:
    print(conta)