from abc import ABC, abstractmethod
class ContaAbstrata(ABC):

    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0

    def creditar(self, valor):
        self._saldo = self._saldo + valor

    @property
    @abstractmethod

    def debitar(self, valor):
        pass
    def get_numero(self):
        return self._numero
    def set_numero(self, numero):
        self._numero = numero
