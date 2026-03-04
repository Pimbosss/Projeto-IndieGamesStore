# classe da conta, recebe numero, usuario e saldo
class ContaBancaria:
    def __init__(self, numero_conta, usuario, saldo=0, ):
        self.numero = numero_conta
        self.usuario = usuario
        self.saldo = int(saldo)
        self.historico = []

    # função depositar, recebe um valor, e salva no historico o valor do depósito
    def depositar(self, valor, ):
        if valor <= 0:
            print("Valor invalido")
            return
        self.saldo += valor
        self.historico.append(f"Deposito: +{valor}")
        print("Depósito realizado com sucesso")

    # função sacar, recebe um valor, e salva no historico o valor do saque
    def sacar(self, valor):
        if valor <= 0:
            print("Valor invalido")
            return
        if valor > self.saldo:
            print("Saldo insuficiente")
            return

        self.saldo -= valor
        self.historico.append(f"Saque: -{valor}")
        print("Saque realizado com sucesso")

    # função transferir, recebe um valor e transfere para outra conta esse valor, e salva no historico o valor da transferencia e quem recebeu
    def transferir(self, valor, outra_conta):
        if valor > self.saldo:
            print("Saldo insuficiente")
            return
        self.saldo -= valor
        outra_conta.saldo += valor
        self.historico.append(f"Transferido: +{valor}")
        outra_conta.historico.append(f"Valor recebido: +{valor} do usuario: {self.usuario}")
        print("Transferido realizado com sucesso")

    # função de ver extrato, exibe tudo que foi feito na conta e mostra o historico
    def exibir_extrato(self):
        print(f"Titular: {self.usuario}")
        print(f"Saldo: {self.saldo}")
        print(f"Historico")
        for itens in self.historico:
            print(itens)


conta1 = ContaBancaria(1, "Heitor", 1000)
conta2 = ContaBancaria(2, "Olívia", 1000)

conta1.exibir_extrato()
conta1.depositar(500)
conta1.transferir(300, conta2)

conta2.exibir_extrato()
conta2.sacar(200)
