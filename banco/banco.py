from POO.conta.conta import Conta

class Banco:

    def __init__(self, numero):

        self.contas = [None]*100
        self.indice = 0

    def Cadastrar(self, conta: Conta):

        self.contas[self.indice] = conta
        self.indice += 1

    def procurar_conta(self, numero):

        i = 0
        achou = False

        while achou is False and i < self.indice:
            if self.contas[i].get_numero() == numero:
                achou = True
            else:
                i += 1
        if achou is True:
            return self.contas[i]
        else:
            return None

    def debitar(self, numero, valor):

        conta = self.procurar_conta(numero)

        if conta:
            conta.debitar(valor)
        else:
            print("Conta Inexistente")

    def creditar(self, numero, valor):

        conta = self.procurar_conta(numero)

        if conta:
            if conta.get_saldo() < valor:
                print('O valor excedeu seu saldo')
            else:
                conta.creditar(valor)
        else:
            print('Conta Inexistente!')

    def saldo(self, numero):

        return self.procurar_conta(numero).get_saldo()

    def transferir(self, origem, destino, valor):

        conta_origem = self.procurar_conta(origem.get_numero())
        conta_destino = self.procurar_conta(destino.get_numero())

        if conta_destino and conta_origem:
            if conta_origem.get_saldo() < valor:
                print('Saldo Insuficiente')
            else:
                conta_origem.debitar(valor)
                conta_destino.creditar(valor)
        else:
            print('Conta Inexistente')
