class Pessoa:
    def __init__(self, nome, cpf, sexo, email):
        self._nome = nome
        self._cpf = cpf
        self.sexo = sexo
        self.email = email
        
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    def __str__(self):
        return f'Nome:{self._nome}\nCPF:{self._cpf}\nSexo:{self._cpf}\nEmail:{self.email}'
    
    def __eq__(self, obj):
        return self._cpf == obj._cpf
    
    def viajar():
        print('Viajou!!!')
# Criando subclasses Professor e Estudante

class Estudante(Pessoa):
    def __init__(self, nome, cpf, sexo, email, matricula, curso):
        super().__init__(nome, cpf, sexo, email)
        self._matricula = matricula
        self.curso = curso
    
    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula
    
    def __str__(self):
        return f'Nome:{self._nome}\nCPF:{self._cpf}\nEmail:{self.email}\nSexo:{self.sexo}\nMatrícula:{self._matricula}\nCurso:{self.curso}'
    
    def assistir_aulas(self):
        print(f"Assistindo aulas de {self.curso}")


class Professor(Pessoa):
    def __init__(self, nome, cpf, sexo, email, salario, formacao):
        super().__init__(nome, cpf, sexo, email)
        self._salario = salario
        self.formacao = formacao
    
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario):
        self._salario = salario
    
    def __str__(self):
        return f'Nome: {self._nome}\nCPF:{self._cpf}\nEmail:{self.email}\nSalário:{self._salario}\nFormação:{self.formacao}'
    
    def assistir_aulas(self):
        print(f"Ministrando aulas de {self.formacao}")


# Testando classes ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

rick = Professor('Rick', 1234567, 'M', 'rick@mail.com', 4000.00, "Tecnologia da Informção")
lara = Estudante('Lara', 7654321, 'F', 'lara@mail.com', 456456467, 'Informática')

print(rick)
print(lara)