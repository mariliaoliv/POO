from POO.conta.contaabstrata import ContaAbstrata
class Conta:

    def __init__(self, numero):
       super().__init__(numero)

    def debitar(self, valor):
        self.__saldo -= valor


