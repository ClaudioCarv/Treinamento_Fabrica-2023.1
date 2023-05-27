class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def emitir_som(self):
        print("O animal está emitindo um som.")
    
    def mover(self):
        print("O animal está se movimentando.")

animal1 = Animal("Leão", 5)
animal1.emitir_som()
animal1.mover()
