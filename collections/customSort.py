#resolver problema da importação
from ..OO import abstractConta

conta_rick = abstractConta.ContaCorrente(3453)
conta_lara = abstractConta.ContaPoupanca(7890)
conta_john = abstractConta.ContaUniversitaria(4456)

contas = [conta_john, conta_lara, conta_rick]

for conta in contas:
    print(conta)