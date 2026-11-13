class Combate :
    def __init__(self, jogador, inimigo) :
        self.jogador = jogador
        self.inimigo = inimigo

    def turno_jogador(self):
        dano = self.jogador.calcular_ataque() #aqui vai pegar o ataque basico do personagem escolhido e vai calcular
        dano_recebido = self.inimigo.receber_dano(dano) #aqui pega a vida do inimigo e calcula o dano que ele recebeu
        
        return dano_recebido

    def turno_inimigo(self):
        if self.inimigo.vida <= 0: #enquanto a vida do inimigo estiver maior que 0 ele ainda pode atacar
            return 0 

        dano = self.inimigo.calcular_ataque()
        dano_recebido = self.jogador.receber_dano(dano)

        return dano_recebido