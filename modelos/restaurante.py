from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): #construtor
        self._nome = nome.title() #self indica do construtor
        self._categoria = categoria.upper()
        self._ativo = False #o _ indica que é um conteudo privado, usuario não modifica
        self._avaliacao = [] #recebe uma lista
        self._cardapio = []
        Restaurante.restaurantes.append(self)
        
    @classmethod #indica que é um metodo da class, um metodo criado por nós, ou seja, uma função
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(20)} | {"Avaliações".ljust(20)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
                        #self significa o objeto
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) #aqui soma a quatidade de notas dentro do obj avaliação
        quantidade_de_notas = len(self._avaliacao) #aqui ve o tanto de avaliação que o restaurante recebeu
        media = round(soma_das_notas / quantidade_de_notas, 1) #o round arredonda o calculo, nesse caso 1 case decimal
        return media
    
    def adicionar_no_cardapio(self,item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'\nCardapio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio,start=1):
            if hasattr(item,'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
