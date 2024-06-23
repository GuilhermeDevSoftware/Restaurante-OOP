from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio): #ItemCardapio significa que é uma herança
    def __init__(self, nome, preco, descricao): 
        super().__init__(nome, preco) #nome e preco vem do ItemCardapio
        self.descricao = descricao

    def __str__(self) :
        return self._nome   
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)