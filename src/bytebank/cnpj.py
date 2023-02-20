from validate_docbr import CNPJ
class Cnpj:
    def __init__(self):
        self._numero = CNPJ().generate()
        
    def valida_cnpj(self, numero):
        return CNPJ().validate(numero)
    
    def gerar_cnpj(self, format=True):
        return CNPJ().generate(format)
    
    def __str__(self):
        return CNPJ().mask(self._numero)