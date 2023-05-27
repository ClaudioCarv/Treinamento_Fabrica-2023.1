class ContaBancaria:
    def __init__(self, nome_titular, numero_conta, saldo=0):
        self.nome_titular = nome_titular
        self.numero_conta = numero_conta
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print("Depósito realizado. Novo saldo:", self.saldo)
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado. Novo saldo:", self.saldo)
        else:
            print("Saldo insuficiente. Operação não realizada.")


conta1 = ContaBancaria("João", "123456", 1000)
conta1.depositar(500)
conta1.sacar(300)
