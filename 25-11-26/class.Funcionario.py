class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base


class Gerente(Funcionario):
    def calcular_salario(self):
        valor_bonus = self.salario_base * 1.20
        print(f"O salario do Gerente {self.nome} é {valor_bonus:.2f}")


class Estagiario(Funcionario):
    def calcular_salario(self):
        salario = self.salario_base
        print(f"O salario de Estagiario {self.nome} é de {salario:.2f}")


G1 = Gerente("Rian", 100)
E1 = Estagiario("Jorge", 100)
E1.calcular_salario()
G1.calcular_salario()