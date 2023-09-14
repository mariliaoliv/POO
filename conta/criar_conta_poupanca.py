from conta_poupanca import ContaPoupanca
class CriarContaPoupanca:
    if __name__ == '__main__':
        poupanca = ContaPoupanca("21.342-7")
        poupanca.creditar(500.87)
        poupanca.debitar(45.00)

        print(poupanca.get_saldo())
