
import abstractConta as conta
from operator import attrgetter


conta_rick = conta.ContaCorrente(3453, "Rick")
conta_lara = conta.ContaPoupanca(7890, "Lara")
conta_john = conta.ContaUniversitaria(4456, "Mary")

contas = [conta_john, conta_lara, conta_rick]

conta_rick.deposita(1000)
conta_lara.deposita(1000)
conta_john.deposita(1000)

for conta in contas:
    print(conta)

# print("-----sort contas by numero-------")
# for conta in sorted(contas, key=attrgetter('numero')):
#     print(conta)

# print("------sort contas by saldo------")
# for conta in sorted(contas, key=attrgetter('_saldo')):
#     print(conta)

print("sort contas default")
for conta in sorted(contas):
    print(conta)


print(conta_john <= conta_rick)