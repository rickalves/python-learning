from classes.funcionario import Funcionario
import pytest
from pytest import mark

# Testes unitário com Pytest
# Metodologia (Given-When-Then)
class TestClass:

    @pytest.fixture
    def funcionario(self):
        return Funcionario("Rick Alves", "20/02/1994", 100000)


    @mark.atributos
    def test_quando_idade_recebe_20_02_1994_deve_retornar_22(self, funcionario):
        esperado = 29
        assert funcionario.idade() == esperado
    
 
    @mark.atributos
    def test_quando_sobrenome_recebe_rick_alves_deve_retornar_alves(self, funcionario):    
        esperado = "Alves"
        assert funcionario.sobrenome() == esperado
    
    @mark.operacoes
    def test_quando_descrescimo_salario_recebe_100000_deve_retornar_90000(self, funcionario):
        esperado = 90000
        funcionario.decrescimo_salario()
        assert funcionario.salario == esperado
    
    @mark.operacoes
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self, funcionario):
        esperado = 100
        funcionario.salario = 1000
        assert funcionario.calcular_bonus() == esperado


    # Test exception on pytest
    @mark.operacoes
    def test_quando_calcular_bonus_recebe_100000_deve_retornar_exception(self, funcionario):
        with pytest.raises(Exception):
            assert funcionario.calcular_bonus()

        
