# 🐍 Jogo da Cobrinha em Python (Curses)

Uma implementação clássica do Jogo da Cobrinha (Snake) desenvolvida em Python, utilizando a biblioteca `curses` para criar a interface e a lógica do jogo diretamente no terminal.

![Gameplay Screenshot](https://github.com/PedroChavesA/Jogo_da_cobrinha/blob/main/pysnake.gif)

## 📜 Sobre o Projeto

Este projeto é uma versão simples e funcional do famoso Jogo da Cobrinha. O jogador controla uma cobra que se move pela tela, com o objetivo de comer as "frutas" que aparecem em locais aleatórios. A cada fruta comida, a cobra cresce em tamanho e a pontuação aumenta. O jogo termina se a cobra colidir com as bordas da tela ou com seu próprio corpo.

O jogo foi desenvolvido para ser executado em um ambiente de linha de comando, oferecendo uma experiência nostálgica e minimalista.

## ✨ Funcionalidades

- **Jogabilidade Clássica:** Controle a cobra e coma as frutas para crescer.
- **Interface no Terminal:** Toda a renderização é feita na janela do terminal usando a biblioteca \`curses\`.
- **Níveis de Dificuldade:** Escolha entre 5 níveis de dificuldade no início do jogo, que ajustam a velocidade da cobra.
- **Sistema de Pontuação:** A pontuação é exibida em tempo real e atualizada a cada fruta consumida.
- **Detecção de Colisão:** O jogo termina se a cobra colidir com as bordas da tela ou consigo mesma.
- **Controles Intuitivos:** Movimente a cobra utilizando as setas do teclado.

## 🚀 Como Executar

Para rodar este projeto, você precisará ter o Python 3 instalado. A biblioteca `curses` já vem pré-instalada na maioria dos sistemas Unix (Linux e macOS).

### Pré-requisitos

- **Python 3.x**

#### Nota para usuários de Windows:
A biblioteca `curses` não está disponível nativamente no Windows. Para rodar o jogo, você precisará instalar o pacote `windows-curses`:
```bash
pip install windows-curses
```

### Passos para a Execução

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/PedroChavesA/Jogo_da_cobrinha
   ```

2. **Navegue até o diretório do projeto:**
   ```bash
   cd seu-repositorio
   ```

3. **Execute o script Python:**
   ```bash
   python pyskane.py
   ```

4. **Siga as instruções no terminal:**
   - Primeiro, você será solicitado a escolher um nível de dificuldade de 1 (lento) a 5 (rápido).
   - A janela do jogo será aberta e você poderá começar a jogar.

## 🕹️ Como Jogar

- **Objetivo:** Comer o máximo de frutas (representadas por `♦`) possível sem colidir.
- **Controles:**
  - **`↑` (Seta para Cima):** Mover para cima
  - **`↓` (Seta para Baixo):** Mover para baixo
  - **`←` (Seta para Esquerda):** Mover para a esquerda
  - **`→` (Seta para Direita):** Mover para a direita
- **Fim de Jogo:** O jogo termina se a cobra tocar nas bordas da tela ou em qualquer parte do seu próprio corpo. Sua pontuação final será exibida.

## 🛠️ Estrutura do Código

O código está organizado em funções modulares para facilitar o entendimento e a manutenção. Aqui está uma visão geral das principais funções:

| Função | Descrição |
| --- | --- |
| \`selecionar_dificuldade()\` | Solicita ao usuário que escolha a dificuldade e retorna a velocidade correspondente. |
| \`ciclo_jogo()\` | É o loop principal do jogo. Controla o estado, o movimento, as colisões e a renderização. |
| \`gerar_nova_fruta()\` | Gera as coordenadas para uma nova fruta em uma posição aleatória na tela. |
| \`mover_cobra()\` | Atualiza as coordenadas da cobra com base na direção atual e verifica se ela cresceu. |
| \`desenhar_mapa()\` | Limpa a tela e desenha as bordas do campo de jogo. |
| \`desenhar_cobra()\` | Renderiza a cobra na tela, com a cabeça (\`@\`) e o corpo (\`s\`). |
| \`desenhar_ator()\` | Função genérica para desenhar qualquer elemento (ator) na tela. |
| \`direcao_e_oposta()\` | Impede que a cobra se mova na direção diretamente oposta à atual. |
| \`cobra_bateu_borda()\` | Verifica se a cabeça da cobra colidiu com as bordas da janela. |
| \`cobra_bateu_em_si()\` | Verifica se a cabeça da cobra colidiu com alguma parte do seu corpo. |
| \`cobra_comeu_fruta()\` | Verifica se a cabeça da cobra está na mesma posição que a fruta. |
| \`finalizar_jogo()\` | Exibe a mensagem de "Você perdeu!" e a pontuação final. |
