class conta:
  
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor

    def get_saldo(self):
        print(f"Saldo atual: {self.saldo}")


minha_conta = conta(100)
minha_conta.depositar(50)
minha_conta.get_saldo()


outra_conta = conta(1000)
outra_conta.get_saldo()