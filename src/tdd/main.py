from src.funcionario import Funcionario

# teste unitário idade
def teste_idade():
    funcionario = Funcionario("Rick", "20/02/1994", 5000.00)
    print(funcionario.idade())

teste_idade()