from gera_doc import GeraDoc

cpf = GeraDoc.gerar_doc('cpf')
cnpj = GeraDoc.gerar_doc('cnpj')

newCPF = cpf.gerar_cpf()

print(cpf)
print(cnpj)
print(newCPF)




