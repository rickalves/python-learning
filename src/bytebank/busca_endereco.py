import requests
class BuscaEndereco:
    def __init__(self, cep, format=False):
        if len(cep) == 8:
            self._cep = cep
            self._format = format
        else:
            raise ValueError('CEP inválido')
    
    def __str__(self):
        if self._format:
            return f'{self._cep[:5]}-{self._cep[5:]}'
        else:
            return self._cep
    
    def buscar(self):
        url = "https://viacep.com.br/ws/{}/json/".format(str(self._cep))
        r = requests.get(url)
        if r.ok:
            endereco = dict(r.json())
            return "{}, {}, {}-{}, {}".format(
                endereco['logradouro'],
                endereco['bairro'],
                endereco['localidade'],
                endereco['uf'], 
                endereco['cep']
                )
        else:
            raise ValueError(f'Erro:{r.status_code}')
