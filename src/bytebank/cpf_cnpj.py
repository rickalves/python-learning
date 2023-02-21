from cpf import Cpf
from cnpj import Cnpj
class GeraDoc:
    
    @staticmethod
    def gerar_doc(tipo):
        if tipo == 'cpf':
            return Cpf()
        elif tipo == 'cnpj':
            return Cnpj()
        else:
            raise AttributeError("Tipo de documento inválido!")
        

       


