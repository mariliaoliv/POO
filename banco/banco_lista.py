from POO.conta.conta import Conta
from POO.conta.conta_poupanca import ContaPoupanca

class Banco:

    def __init__(self, numero):
        self.contas = []

    def Cadastrar(self, conta: Conta):
        self.contas.append(conta)

    def procurar_conta(self, numero):
        for conta in self.contas:
            if conta.get_numero() == numero:
                return conta
            else:
                return 'Conta não encontrada'

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
            if conta_origem.get_saldo() <= valor:
                print('Saldo Insuficiente')
            else:
                conta_origem.debitar(valor)
                conta_destino.creditar(valor)
        else:
            print('Conta Inexistente')

    def render_juros(self, numero):
        analise_conta = self.procurar_conta(mumero).get_numero()

        if analise_conta:
            if isinstance(analise_conta, ContaPoupanca):
                analise_conta.render_juros(self.juros)

            else:
                 print('Operação Inválida')
        else:
            print("Conta Inexistente")






