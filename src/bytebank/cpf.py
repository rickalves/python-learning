from validate_docbr import CPF
class Cpf:
    def __init__(self):
        self._numero = CPF().generate()
        
    def valida_cpf(self, numero):
        return CPF().validate(numero)
    
    def gerar_cpf(self, format=False):
        return CPF().generate(format)
    
    def __str__(self):
        return CPF().mask(self._numero)