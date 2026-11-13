
from classes.inimigo import Inimigo


class Goblin(Inimigo):
    def __init__(self, nome, vida, dano):
        super().__init__(nome, vida, dano)



class GoblinComum(Goblin):
    def __init__(self):
        super().__init__("Goblin Comum", 60, 20)



class GoblinGuerreiro(Goblin):
    def __init__(self):
        super().__init__("Goblin Guerreiro", 80, 30)



class GoblinChefe(Goblin):
    def __init__(self):
        super().__init__("Goblin Chefe", 160, 40)
