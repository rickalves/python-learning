
# URL example
# url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"
url = ""

# url sanitization
if url.strip() == "":
    raise ValueError('Empty URL!')
else:
    # Break url in base and parameters
    urlBreak = url.find('?')
    urlBase = url[:urlBreak]
    urlParams = url[urlBreak+1:]

    # Extract params values
    paramSearch = 'moedaDestino'
    paramIndex = urlParams.find(paramSearch)
    valueIndex = paramIndex + len(paramSearch)+1
    paramsBreak = urlParams.find('&', valueIndex)

    if paramsBreak == -1:
        paramValue = urlParams[valueIndex:]
    else:
        paramValue = urlParams[valueIndex:paramsBreak]

    # print param value
    print(paramValue)

