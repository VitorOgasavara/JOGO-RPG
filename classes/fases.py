from classes.goblin import GoblinComum, GoblinGuerreiro, GoblinChefe

class Fases:
    def fase_1(self):
        return [GoblinComum() for numero in range(6)] #aqui faz dar aparecer 6 goblins comun na primeira fase

    def fase_2(self):
        return [GoblinComum(), GoblinComum(), GoblinGuerreiro(),GoblinComum(), GoblinComum(), GoblinGuerreiro(),GoblinComum(), GoblinGuerreiro(),]  

    def fase_3(self):
        return [GoblinComum(), GoblinGuerreiro(), GoblinGuerreiro(), GoblinComum(), GoblinGuerreiro(), GoblinGuerreiro(),GoblinComum(), GoblinGuerreiro(), GoblinGuerreiro(),GoblinChefe()]
