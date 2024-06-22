from modelos.restaurante import Restaurante

restaurante_padoca = Restaurante('Padoca', 'Padaria')
restaurante_mexicano = Restaurante('Mexican food', 'Mexicano')
restaurante_pizza = Restaurante('Pizzaria Italy', 'Pizzaria')
restaurante_hamburguer = Restaurante('Hamburgueria El', 'Hamburgueria')

restaurante_padoca.receber_avaliacao('Guilherme', 10)
restaurante_padoca.receber_avaliacao('Lais', 8)
restaurante_padoca.receber_avaliacao('Jorge', 7.5)

restaurante_mexicano.receber_avaliacao('Silvia', 9)
restaurante_mexicano.receber_avaliacao('Gabriel', 2)
restaurante_mexicano.receber_avaliacao('Jeremias', 5)

restaurante_pizza.receber_avaliacao('Rodrigo', 10)
restaurante_pizza.receber_avaliacao('Camila', 6)
restaurante_pizza.receber_avaliacao('William', 8)

restaurante_hamburguer.receber_avaliacao('Jaqueline', 4)
restaurante_hamburguer.receber_avaliacao('Larissa', 7)
restaurante_hamburguer.receber_avaliacao('Emmily', 10)

restaurante_hamburguer.alternar_estado()
restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()