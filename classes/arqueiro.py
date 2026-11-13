from classes.personagem import Personagem

class Arqueiro(Personagem):
    def __init__(self):
        super().__init__("Arqueiro", 120, 30)