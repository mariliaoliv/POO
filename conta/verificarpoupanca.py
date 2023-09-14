from conta import Conta
from conta_poupanca import ContaPoupanca

class VerificaPopanca:
    if __name__ == '__main__':
        opcao = int(input("Escolha: [1] Conta e [2] Poupança"))
        if opcao == 1:
            conta = Conta("21.342-7")

        else:
            conta = ContaPoupança("21.432-7")

        conta.creditar(500.87)
        conta.debitar(45.00)

        if isinstance(conta, ContaPoupaca):
            conta.render_juros(0.1)
            print("Saldo com juros: {}".format(conta.get_saldo()))

