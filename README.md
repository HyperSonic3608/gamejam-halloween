# 🎃 Halloween em Moscow

Um jogo de mistério e exploração 2D desenvolvido em **Python** utilizando a biblioteca **Pygame**, criado especialmente para a **Game Jam Carol Carvalho - Halloween**.

---

## 📸 Sobre o Jogo

Em uma noite de Halloween, um guarda soviético adormece durante seu turno e desperta em uma Moscou estranhamente silenciosa, tomada por decorações de Halloween e uma atmosfera inquietante. Enquanto explora a cidade e seus ambientes abandonados, ele encontra enigmas, passagens misteriosas e pistas que parecem desafiar a realidade. Resolva os desafios e descubra o que está acontecendo nesta noite em que sonho e realidade se confundem.

### 🌟 Destaques

- **Exploração e Interação:** Diversas ambientações e cenários conectadas.
- **Puzzles e Minijogos:** Desafios variados como caça-palavras, senhas de cadeados e enigmas contextuais.
- **Arte e Animações:** Animações de movimentação do personagem, elementos visuais temáticos e pistas espalhadas pelo mapa.

---

## 🔗 Links Relevantes

- 🎮 **Página do Jogo (Itch.io):** [Halloween em Moscow](https://mateusem.itch.io/halloween-em-moscow)
- 🏆 **Página da Game Jam:** [Game Jam Carol Carvalho - Halloween](https://itch.io/jam/halloween-carol-carvalho)

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Engine/Biblioteca:** Pygame

---

## 📁 Estrutura do Projeto

```text
gamejam-halloween/
├── cenarios/              # Módulos de mapas, cenários e minijogos (puzzle, cadeado, caça-palavras, etc.)
├── sprites/               # Sprites de personagens, objetos, pistas e animações
├── main.py                # Ponto de entrada principal do jogo
├── menu.py                # Interface do menu do jogo
├── personagem.py          # Lógica e movimentação do jogador
├── requirements.txt       # Dependências do projeto (Pygame)
└── .gitignore
```

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos

- **Python 3.x** instalado.

### Passo a passo

1. **Clone o repositório:**

```bash
git clone https://github.com/mateusem/halloween-em-moscow.git
cd halloween-em-moscow
```

2. **Crie e ative um ambiente virtual (opcional):**

- **Linux/macOS:**

```bash
python -m venv venv
source venv/bin/activate
```

- **Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Execute o jogo:**

```bash
python main.py
```
