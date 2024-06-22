from modelos.restaurante import Restaurante

restaurante_padoca = Restaurante('Padoca', 'Padaria')
restaurante_mexicano = Restaurante('Mexican food', 'Mexicano')
restaurante_japones = Restaurante('Japa food', 'Japonês')

restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()