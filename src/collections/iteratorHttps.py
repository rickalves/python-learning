class IteradorHttp():
    def __init__(self):
        self.registro = open('./src/collections/acessos.log', 'r')
        self.linha_atual = ''
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.linha_atual = self.registro.readline()
        while self.linha_atual and not self.linha_atual.startswith('http://'):
            self.linha_atual = self.registro.readline()
        if self.linha_atual:
            return self.linha_atual
        raise StopIteration

iteradorURL = IteradorHttp()

# print(next(iterador))
# print(next(iterador))
# print(next(iterador, 'Fim do iterator'))

for url in iteradorURL:
    print(url)