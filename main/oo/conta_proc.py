def cria_conta(numero, titular, saldo, limite):
    conta = {"numero":numero, "titular":titular, "saldo":saldo, limite:limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def novoLimite(conta, valor):
    conta["limite"] = valor

def transferir(contaOrigen, contaDestino, valor):
    contaOrigen["saldo"] -= valor
    contaDestino["saldo"] +- valor
    
def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))