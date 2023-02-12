class UrlExtractor:
    def __init__(self, url):
        self.url = url
        self._urlBreak = url.find('?')

    
    def validade_url(self)->bool:
        if self.url.strip() == "":
            return False
        else:
            return True
    
    def get_url_base(self)->str:
        return self.url[:self._urlBreak]
    
    def get_url_params(self)->str:
        return self.url[self._urlBreak+1:]
    
    def find_param(self, param)->bool:
        return self.get_url_params().find(param) != -1 if True else False

    def get_param_value(self, param)->str:
        paramValue = ''
        paramIndex = self.get_url_params().find(param)
        valueIndex = paramIndex + len(param)+1
        paramsBreak = self.get_url_params().find('&', valueIndex)
        if paramsBreak == -1:
            paramValue = self.get_url_params()[valueIndex:]
        else:
            paramValue = self.get_url_params()[valueIndex:paramsBreak]

        return paramValue

# Class test
url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"
extract_url = UrlExtractor(url)

print(extract_url.find_param('quantidade'))