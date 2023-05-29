class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("O carro está ligado.")
        else:
            print("O carro já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print("O carro está desligado.")
        else:
            print("O carro já está desligado.")

    def acelerar(self, velocidade):
        if self.ligado:
            self.velocidade += velocidade
            print(f"O carro acelerou para {self.velocidade} km/h.")
        else:
            print("O carro precisa estar ligado para acelerar.")



meu_carro = Carro("Ford", "Focus", 2022)
meu_carro.ligar()  
meu_carro.acelerar(30)  
meu_carro.acelerar(20)  
meu_carro.desligar()  
