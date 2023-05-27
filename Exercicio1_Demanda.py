class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def imprimir(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
pessoa1 = Pessoa("Pedro", 23)
pessoa1.imprimir()
