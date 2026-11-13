from flask import Flask, render_template, redirect, url_for, session
from random import randint

app = Flask(__name__)
app.secret_key = 'troque-esta-chave-por-uma-chave-secreta'

HEROIS = {
    'guerreiro': {'nome': 'Guerreiro', 'vida_maxima': 150, 'dano': 35},
    'mago': {'nome': 'Mago', 'vida_maxima': 100, 'dano': 45},
    'arqueiro': {'nome': 'Arqueiro', 'vida_maxima': 120, 'dano': 40},
}

INIMIGOS = {
    1: {'tipo': 'comum', 'nome': 'Goblin Comum', 'vida_maxima': 60, 'dano': 20, 'imagem': 'imagens/inimigos/goblincomun.png', 'quantidade': 6, 'xp': 25},
    2: {'tipo': 'guerreiro', 'nome': 'Goblin Guerreiro', 'vida_maxima': 80, 'dano': 30, 'imagem': 'imagens/inimigos/goblinguerreiro.png', 'quantidade': 8, 'xp': 35},
    3: {'tipo': 'chefe', 'nome': 'Goblin Chefe', 'vida_maxima': 160, 'dano': 40, 'imagem': 'imagens/inimigos/goblinchefe.png', 'quantidade': 10, 'xp': 50},
}


def xp_necessario(jogo):
    return 100 * jogo['nivel']


def criar_inimigo(fase):
    config = INIMIGOS[fase]
    return {chave: config[chave] for chave in ('tipo', 'nome', 'vida_maxima', 'dano', 'imagem')} | {'vida': config['vida_maxima']}


def novo_jogo(classe):
    dados = HEROIS[classe]
    return {
        'classe': classe,
        'nome': dados['nome'],
        'vida': dados['vida_maxima'],
        'vida_maxima': dados['vida_maxima'],
        'dano': dados['dano'],
        'nivel': 1,
        'xp': 0,
        'pocoes': 3,
        'fase': 1,
        'inimigo_numero': 1,
        'inimigo': criar_inimigo(1),
        'mensagem': 'A batalha começou!',
        'estado': 'batalha',
        'ultima_acao': '',
    }


def guardar(jogo):
    session['jogo'] = jogo
    session.modified = True


def jogo_atual():
    return session.get('jogo')


def pagina_atual(jogo):
    if not jogo:
        return redirect(url_for('selecionar'))
    estado = jogo.get('estado', 'batalha')
    if estado == 'gameover':
        return render_template('gameover.html')
    if estado == 'vitoria1':
        return render_template('vitoria1.html', jogo=jogo)
    if estado == 'vitoria2':
        return render_template('vitoria2.html', jogo=jogo)
    if estado == 'vitoria3':
        return render_template('vitoria3.html', jogo=jogo)
    if estado == 'final':
        return render_template('final.html', jogo=jogo)
    return render_template(f"fase{jogo['fase']}.html", jogo=jogo, xp_meta=xp_necessario(jogo))


def destino(jogo):
    guardar(jogo)
    return redirect(url_for(f"fase{jogo['fase']}"))


def subir_nivel(jogo):
    niveis = 0
    while jogo['xp'] >= xp_necessario(jogo):
        jogo['xp'] -= xp_necessario(jogo)
        jogo['nivel'] += 1
        jogo['vida_maxima'] += 20
        jogo['dano'] += 5
        jogo['vida'] = min(jogo['vida_maxima'], jogo['vida'] + 20)
        niveis += 1
    return niveis


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/selecionar')
def selecionar():
    return render_template('selecionar.html')


@app.route('/personagem/<classe>')
def personagem(classe):
    if classe not in HEROIS:
        return redirect(url_for('selecionar'))
    # O template usa jogador.__class__.__name__. Um tipo com o nome da classe
    # permite mostrar o sprite correspondente sem alterar personagem.html.
    dados = HEROIS[classe]
    tipo = type(classe.capitalize(), (), {})
    jogador = tipo()
    jogador.nome = dados['nome']
    jogador.vida_maxima = dados['vida_maxima']
    jogador.dano = dados['dano']
    jogador.nivel = 1
    return render_template('personagem.html', jogador=jogador)


@app.route('/iniciar-fase1/<classe>')
def iniciar_fase1(classe):
    if classe not in HEROIS:
        return redirect(url_for('selecionar'))
    guardar(novo_jogo(classe))
    return redirect(url_for('fase1'))


@app.route('/fase1')
def fase1():
    return pagina_atual(jogo_atual())


@app.route('/fase2')
def fase2():
    return pagina_atual(jogo_atual())


@app.route('/fase3')
def fase3():
    return pagina_atual(jogo_atual())


@app.route('/atacar', methods=['POST'])
def atacar():
    jogo = jogo_atual()
    if not jogo:
        return redirect(url_for('selecionar'))
    if jogo['estado'] != 'batalha':
        return pagina_atual(jogo)

    inimigo = jogo['inimigo']
    dano = randint(max(1, jogo['dano'] - 5), jogo['dano'] + 5)
    inimigo['vida'] = max(0, inimigo['vida'] - dano)
    mensagem = f"Você causou {dano} de dano em {inimigo['nome']}!"

    if inimigo['vida'] == 0:
        jogo['xp'] += INIMIGOS[jogo['fase']]['xp']
        niveis = subir_nivel(jogo)
        if niveis:
            mensagem += f' Você subiu {niveis} nível(is)!'
        if jogo['inimigo_numero'] >= INIMIGOS[jogo['fase']]['quantidade']:
            jogo['estado'] = f"vitoria{jogo['fase']}"
            mensagem += ' Fase concluída!'
        else:
            jogo['inimigo_numero'] += 1
            jogo['inimigo'] = criar_inimigo(jogo['fase'])
            mensagem += ' Um novo inimigo apareceu!'
    else:
        dano_inimigo = randint(max(1, inimigo['dano'] - 5), inimigo['dano'] + 5)
        jogo['vida'] = max(0, jogo['vida'] - dano_inimigo)
        mensagem += f' O inimigo causou {dano_inimigo} de dano em você.'
        if jogo['vida'] == 0:
            jogo['estado'] = 'gameover'
            mensagem += ' Você foi derrotado.'

    jogo['mensagem'] = mensagem
    jogo['ultima_acao'] = 'atacar'
    guardar(jogo)
    return redirect(url_for(f"fase{jogo['fase']}"))


@app.route('/usar-pocao', methods=['POST'])
def usar_pocao():
    jogo = jogo_atual()
    if not jogo:
        return redirect(url_for('selecionar'))
    if jogo['estado'] != 'batalha':
        return pagina_atual(jogo)

    if jogo['pocoes'] <= 0:
        jogo['mensagem'] = 'Você não tem mais poções.'
    elif jogo['vida'] >= jogo['vida_maxima']:
        jogo['mensagem'] = 'Sua vida já está cheia.'
    else:
        cura = min(50, jogo['vida_maxima'] - jogo['vida'])
        jogo['vida'] += cura
        jogo['pocoes'] -= 1
        jogo['mensagem'] = f'Você recuperou {cura} pontos de vida.'
    jogo['ultima_acao'] = 'pocao'
    return destino(jogo)


def avancar(jogo, proxima_fase, estado_esperado):
    if not jogo:
        return redirect(url_for('selecionar'))
    if jogo['estado'] != estado_esperado:
        return pagina_atual(jogo)
    jogo['fase'] = proxima_fase
    jogo['inimigo_numero'] = 1
    jogo['inimigo'] = criar_inimigo(proxima_fase)
    jogo['estado'] = 'batalha'
    jogo['vida'] = jogo['vida_maxima']
    jogo['pocoes'] += 2
    jogo['mensagem'] = f'Fase {proxima_fase} iniciada!'
    return destino(jogo)


@app.route('/avancar-fase2', methods=['POST'])
def avancar_fase2():
    return avancar(jogo_atual(), 2, 'vitoria1')


@app.route('/avancar-fase3', methods=['POST'])
def avancar_fase3():
    return avancar(jogo_atual(), 3, 'vitoria2')


@app.route('/mostrar-final', methods=['POST'])
def mostrar_final():
    jogo = jogo_atual()
    if not jogo:
        return redirect(url_for('selecionar'))
    if jogo['estado'] != 'vitoria3':
        return pagina_atual(jogo)
    jogo['estado'] = 'final'
    guardar(jogo)
    return redirect(url_for('final'))


@app.route('/final')
def final():
    return pagina_atual(jogo_atual())


@app.route('/tentar-novamente', methods=['POST'])
def tentar_novamente():
    session.pop('jogo', None)
    return redirect(url_for('selecionar'))


@app.route('/reiniciar-jogo', methods=['POST'])
def reiniciar_jogo():
    session.pop('jogo', None)
    return redirect(url_for('selecionar'))


if __name__ == '__main__':
    app.run(debug=True)