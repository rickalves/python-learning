import re
class Telefone:
    def __init__(self, numero):
        if self.valida_telefone(numero):
            self._numero = self.valida_telefone(numero)
        else:
            raise ValueError('Telefone Inválido')

    def valida_telefone(self, numero):
        numero_valido = re.search("([0-9]{3})?([0-9]{2})([0-9]{4,5})([0-9]{4})", numero)
        if numero_valido:
            return numero_valido
        else:
            return False

    def __str__(self):
        if self._numero.group(1):
            return f'+{self._numero.group(1)}({self._numero.group(2)}){self._numero.group(3)}-{self._numero.group(4)}'
        else:
            return f'({self._numero.group(2)}){self._numero.group(3)}-{self._numero.group(4)}'


    