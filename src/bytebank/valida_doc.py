import validate_docbr as docbr
class ValidaDoc:
    def __init__(self, tipo):
        self._tipo = tipo
        if tipo == 'cpf':
            self._numero = docbr.CPF().generate()
        elif tipo == 'cnpj':
            self._numero = docbr.CNPJ().generate()
        else:
            raise AttributeError("Tipo de documento inválido!")
        
    def validar_doc(self, numero, tipo):
        if tipo == 'cpf':
            return docbr.CPF().validate(numero)
        elif tipo == 'cnpj':
            return docbr.CNPJ().validate(numero)
        else:
            raise AttributeError("Tipo de documento inválido!")

    def gerar_doc(self, tipo):
        if tipo == 'cpf':
            self._numero = docbr.CPF().generate()
        elif tipo == 'cnpj':
            self._numero = docbr.CNPJ().generate()
        else:
            raise AttributeError("Tipo de documento inválido!")
    
    def __str__(self):
        if self._tipo == 'cpf':
            return docbr.CPF().mask(self._numero)
        else:
            return docbr.CNPJ().mask(self._numero)


