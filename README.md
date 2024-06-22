# Projeto de Programação Orientada a Objetos com Python

## Descrição

Este projeto demonstra os conceitos de programação orientada a objetos (POO) usando Python. Ele inclui uma classe `Restaurante` que modela o comportamento e as propriedades de um restaurante. A classe permite a criação de instâncias de restaurantes, listagem de todos os restaurantes e alteração do estado (ativo/inativo) dos restaurantes.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- **modelos/restaurante.py**: Contém a definição da classe `Restaurante`.
- **main.py**: Script principal para executar e testar a funcionalidade da classe `Restaurante`.

## Funcionalidades

- **Classe Restaurante**:
  - `__init__(self, nome, categoria)`: Construtor que inicializa o nome e a categoria do restaurante.
  - `__str__(self)`: Retorna uma representação em string legível da instância do restaurante.
  - `listar_restaurantes(cls)`: Método de classe que lista todos os restaurantes.
  - `ativo`: Propriedade que retorna o estado do restaurante (ativo ou inativo) em forma de símbolo.
  - `alternar_estado(self)`: Alterna o estado do restaurante entre ativo e inativo.

## Como Usar

### Pré-requisitos

- Python 3.x instalado

