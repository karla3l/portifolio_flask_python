""" Usando Python, crie uma classe Carro que encapsule os atributos e métodos necessários para
permitir que o usuário mova uma instância desse objeto em um grid de tags "div". 
O usuário terá duas ações a sua disposição: "virar a direita" e "virar a esquerda", 
podendo mover a instância para qualquer posição de um tabuleiro de 10 linhas e 10 colunas de "divs".
Cada movimento feito pelo usuário deve ser atualizado na instância.
A classe deve armazenar um histórico dos movimentos feitos pelo usuário.
Quando o usuário escolher opção para encerrar a aplicação, o histórico de valores alterados dos
atributos da instância devem ser exibidos na tela para comprovar que todos os movimentos foram armazenados no objeto. """

class Carro:
    def __init__(self):
        self.carro = []


