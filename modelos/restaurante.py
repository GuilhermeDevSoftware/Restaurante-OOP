class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): #construtor
        self._nome = nome.title() #self indica do construtor
        self._categoria = categoria.upper()
        self._ativo = False #o _ indica que é um conteudo privado, usuario não modifica
        Restaurante.restaurantes.append(self)

    def __str__(self): #Para mostrar como string, legivel para nós
        return f'{self._nome} || {self._categoria}'   
    
    @classmethod #indica que é um metodo da class, um metodo criado por nós, ou seja, uma função
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(20)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

