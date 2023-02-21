from classes.funcionario import Funcionario
# Testes unitário com Pytest
# Metodologia (Given-When-Then)
class TestClass:

    def test_quando_idade_recebe_20_02_1994_deve_retornar_22(self):
        #Given
        entrada = '20/02/1994'
        esperado = 29

        funcionario = Funcionario("Rick", entrada, 1000)
        # When
        resultado = funcionario.idade()
        # Then
        assert resultado == esperado


