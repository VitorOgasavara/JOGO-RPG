from classes.personagem import Personagem # aqui estamos puxando a classe personagem de outro arquivo para utilizarmos no guerreio


class Guerreiro(Personagem):
    def __init__(self):
        super().__init__("Guerreiro", 150, 30) # aqui nos estamos definindo o nome, vida e dano