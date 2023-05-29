class PessoaFisica:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def imprimir_informacoes(self):
        print("Informações da Pessoa Física:")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Idade: {self.idade}")



pessoa = PessoaFisica("Cláudio", "123.456.789-99", 20)
pessoa.imprimir_informacoes()
