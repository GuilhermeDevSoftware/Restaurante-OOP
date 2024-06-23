from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):  #Siginifica que todas as derivadas dela terá essa função
        pass #não preciso colocar o código aqui, ela apenas indica que todos teram essa classe