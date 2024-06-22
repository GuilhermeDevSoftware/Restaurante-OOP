from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): #construtor
        self._nome = nome.title() #self indica do construtor
        self._categoria = categoria.upper()
        self._ativo = False #o _ indica que é um conteudo privado, usuario não modifica
        self._avalicao = [] #recebe uma lista
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
        avaliacao = Avaliacao(cliente, nota)
        self._avalicao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avalicao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avalicao) #aqui soma a quatidade de notas dentro do obj avaliação
        quantidade_de_notas = len(self._avalicao) #aqui ve o tanto de avaliação que o restaurante recebeu
        media = round(soma_das_notas / quantidade_de_notas, 1) #o round arredonda o calculo, nesse caso 1 case decimal
        return media