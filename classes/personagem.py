import random

class Personagem:
    def __init__(self, nome, vida_maxima, dano):

        # identificar nome
        self.nome = nome 

        # combate
        self.vida_maxima = vida_maxima
        self.dano = dano
        self.vida = vida_maxima
        
        # sistema de xp
        self.xp = 0
        self.nivel = 1

        # o que vai começar no inventario
        self.pocoes = 1

    def receber_dano(self, quantidade):
        if quantidade < 0:
            raise ValueError("O dano não pode ser negativo") # isso é para nao tomar dano negativo

        dano_recebido = min(quantidade, self.vida) # ex: Guerreiro tem 30 HP e recebe um ataque de 50 ele so pega o minimo e recebe só 30 de dano
        self.vida -= dano_recebido

        return dano_recebido
    
    def curar(self, quantidade):
        if quantidade < 0 :
             raise ValueError("A cura não pode ser negativa")

        vida_anterior = self.vida
        self.vida = min(self.vida + quantidade, self.vida_maxima)

        return self.vida - vida_anterior

    def adicionar_xp(self, quantidade):
        if quantidade < 0 :
            raise ValueError("O xp não pode ser negativo")

        self.xp += quantidade

        niveis = { 2 : 100, 3 : 250, 4 : 450, 5: 700} # aqui ta mostrando quanto de xp vc precisa ter paara passar de nivel

        while self.nivel < 5 :
            proximo_nivel = self.nivel + 1  # aqui calcula o nivel

            if self.xp >= niveis[proximo_nivel] : # [] serve pra busca o nivel
                self.nivel = proximo_nivel
                self.vida_maxima += 20 #aqui mostra o quanto que vai aumentar a vida e o dano por nivel
                self.dano += 5 # o ataque aumenta ao upar
                self.vida = min(self.vida + 30, self.vida_maxima) # ele ganha mais 30 de vida no meio do combate, a função min nao deixa passar o limite da sua vida maxima
            else: break
            
    def calcular_ataque(self): # randomiza o ataque do personagem de acordo como seu ataque base
        dano_minimo = max(1, self.dano - 5)
        dano_maximo = self.dano + 5

        return random.randint(dano_minimo, dano_maximo)

    def usar_pocao(self):
        if self.pocoes <= 0: #aqui verifica se tem poções
         return 0

        if self.vida >= self.vida_maxima: # aqui verifica se a vida ta cheia ou nao
            return 0

        quantidade = random.randint(60,70) #aqui é onde randomiza qaunto a poção vai curar
        vida_recuperada = self.curar(quantidade) #aqui cura o personagem

        self.pocoes -= 1 #aqui tira gasta a poção do inventario (gasta -1)

        return vida_recuperada

