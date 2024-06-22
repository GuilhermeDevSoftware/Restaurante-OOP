from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_padoca = Restaurante('Padoca', 'Padaria')
bebida_suco = Bebida('Suco de Melancia', 4.70, 'G')
prato_pao = Prato('Pao doce', 5.30, 'O melhor pão doce da cidade')
restaurante_padoca.adicionar_no_cardapio(bebida_suco)
restaurante_padoca.adicionar_no_cardapio(prato_pao)

def main():
    restaurante_padoca.exibir_cardapio

if __name__ == '__main__':
    main()