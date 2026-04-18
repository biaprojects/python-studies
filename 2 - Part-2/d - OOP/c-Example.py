# Exercise developed during a univesp class

class Funcionario:
    def __init__(self, nome, data_admissao, salario):
        self.nome = nome
        self.data_admissao = data_admissao
        self.salario = salario

    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_data_admissao(self):
        return self.data_admissao
    
    def get_salario(self):
        return self.salario

    def set_salario(self, salario):
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, nome, data_admissao, salario, bonus):
        super().__init__(nome, data_admissao, salario)
        self.bonus = bonus

    def get_bonus(self):
        return self.bonus

    def set_bonus(self, bonus):
        self.bonus = bonus
    
    def get_salario_com_bonus(self):
        return self.salario + (self.bonus/100 * self.salario)
    