# ⚔️ Reino das Sombras 👑

## 🎮 Sobre o jogo

**Reino das Sombras** é um RPG de batalha por turnos desenvolvido em Python, utilizando o framework Flask, HTML e CSS.

O jogador escolhe um herói e enfrenta diferentes inimigos ao longo de três fases, evoluindo seu personagem até chegar à batalha final.

## 🛡️ Personagens

O jogador pode escolher entre três classes:

- ⚔️ **Guerreiro** — Um combatente especializado em ataques físicos.
- 🔮 **Mago** — Um personagem que utiliza poderes mágicos.
- 🏹 **Arqueiro** — Um herói especializado em ataques à distância.

Cada classe possui seus próprios atributos de vida e dano.

## 👹 Inimigos

Durante a aventura, o jogador enfrenta:

- Goblin Comum
- Goblin Guerreiro
- Goblin Chefe

## 🏰 Fases do jogo

**Fase 1 — Floresta Sombria**

O jogador enfrenta 6 inimigos.

**Fase 2 — Terras Amaldiçoadas**

O jogador enfrenta 8 inimigos.

**Fase 3 — Batalha Final**

O jogador enfrenta 10 inimigos e precisa superar o desafio final.

## ✨ Funcionalidades

- Escolha de personagens
- Sistema de combate por turnos
- Barras de vida
- Sistema de experiência (XP)
- Evolução de nível
- Poções para recuperar vida
- Telas de vitória e Game Over
- Botões animados com estilo medieval
- Possibilidade de escolher outro personagem e recomeçar

## 💻 Tecnologias utilizadas

- Python
- Flask
- HTML
- CSS


## 📁 Estrutura do projeto

```text
Reino-das-Sombras/
├── app.py
├── requirements.txt
├── README.md
├── classes/
├── templates/
│   ├── index.html
│   ├── selecionar.html
│   ├── personagem.html
│   ├── fase1.html
│   ├── fase2.html
│   ├── fase3.html
│   ├── vitoria1.html
│   ├── vitoria2.html
│   ├── vitoria3.html
│   ├── gameover.html
│   └── final.html
└── static/
    ├── css/
    │   └── style.css
    └── imagens/
```

## 🚀 Como executar o jogo

**1.** Instale o Python no computador.

**2.** Abra a pasta do projeto no VS Code.

**3.** Instale as dependências:

```bash
pip install -r requirements.txt
```

**4.** Execute o jogo:

```bash
python app.py
```

**5.** Abra o navegador e acesse:

http://127.0.0.1:5000/

## 🎯 Como jogar

1. Clique em **INICIAR JOGO**.
2. Escolha Guerreiro, Mago ou Arqueiro.
3. Clique em **INICIAR AVENTURA**.
4. Utilize o botão **ATACAR** para enfrentar os inimigos.
5. Utilize **USAR POÇÃO** para recuperar vida quando necessário.
6. Derrote os inimigos e avance pelas três fases.
7. Vença a batalha final para concluir o jogo.

Se perder, você poderá escolher outro personagem e tentar novamente.

## 👑 Objetivo

Derrotar as forças das trevas, superar os desafios das três fases e conquistar a vitória no Reino das Sombras.


