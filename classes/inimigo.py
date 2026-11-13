import random

class Inimigo :
    def __init__(self, nome, vida_maxima, dano) :
         self.nome = nome
         self.vida_maxima = vida_maxima
         self.vida = vida_maxima
         self.dano = dano
        

    def receber_dano(self,quantidade):
        if quantidade < 0:
            raise ValueError ("O dano não pode ser negativo")

        dano_recebido = min(quantidade, self.vida)
        self.vida -= dano_recebido

        return dano_recebido

    def calcular_xp(self): # aqui estou randomizando o xp 
        return random.randint (30, 50)

    def calcular_ataque(self): # aqui estou rendomizando o ataque do inimigo
        dano_minimo = self.dano
        dano_maximo = self.dano + 5

        return random.randint(dano_minimo, dano_maximo)

    
    def dropar_pocao(self): # nesse def o random vai escolher um numero de 1 a 100, se cair entre 1 e 70, o jogador ganha uma poçao de cura
        chance = random.randint(1, 100)

        if chance <= 70:
            return random.randint(1,3)

        return 0
