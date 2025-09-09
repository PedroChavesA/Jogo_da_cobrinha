import curses
import random
import time

def ciclo_jogo(janela, velocidade_jogo): 
    """
    Inicia o loop principal do jogo, em que a cobra move-se
    em resposta a comandos do usu rio e vai crescendo
    caso coma a fruta.

    - `janela` : objeto que representa a janela do jogo
    - `velocidade_jogo` : velocidade em que o jogo ser  atualizado

    :return: None
    """
    curses.curs_set(0)
    janela.nodelay(1)
    janela.timeout(velocidade_jogo)

    
    cobra = [ [10, 15], [9, 15], [8, 15] ]
    fruta = gerar_nova_fruta(janela=janela)
    direcao_atual = curses.KEY_DOWN
    pontuacao = 0
    
    cobra_cresce_nesta_rodada = False

    while True:
        desenhar_mapa(janela=janela)
        desenhar_cobra(cobra=cobra, janela=janela)
        desenhar_ator(ator=fruta, janela=janela, caracter=curses.ACS_DIAMOND)
        janela.addstr(0, 5, f' Pontuação: {pontuacao} ')

        nova_direcao = janela.getch()
        
        if nova_direcao == -1:
            nova_direcao = direcao_atual
        elif direcao_e_oposta(nova_direcao, direcao_atual):
            nova_direcao = direcao_atual
        
        direcao_atual = nova_direcao

        mover_cobra(cobra=cobra, direcao=direcao_atual, cobra_comeu_fruta=cobra_cresce_nesta_rodada)

        if cobra_bateu_borda(cobra=cobra, janela=janela):
            break
        if cobra_bateu_em_si(cobra=cobra):
            break

        if cobra_comeu_fruta(cobra=cobra, fruta=fruta):
            pontuacao += 1
            cobra_cresce_nesta_rodada = True
            fruta = gerar_nova_fruta(janela=janela)
        else:
            cobra_cresce_nesta_rodada = False
        
        janela.refresh()

    finalizar_jogo(pontuacao=pontuacao, janela=janela)

def mover_cobra(cobra, direcao, cobra_comeu_fruta):    
    """
    Move a cobra de acordo com a direção e verifica se a cobra cresceu.

    - `cobra` : lista de coordenadas que representam a cobra
    - `direcao` : dire o em que a cobra deve ser movida
    - `cobra_comeu_fruta` : booleano que indica se a cobra cresceu

    :return: None
    """
    cabeça = cobra[0].copy()
    mover_ator(ator=cabeça, direcao=direcao)
    cobra.insert(0, cabeça)

    if not cobra_comeu_fruta:
        cobra.pop()

def gerar_nova_fruta(janela):
    """
    Gera uma nova fruta em uma posição aleatória na tela.

    A posição gerada é uma lista com dois elementos, o primeiro é a altura (linha) e o
    segundo é a largura (coluna).

    A altura e a largura são geradas com o módulo random.randint e limitadas às bordas da
    tela, tendo como origem o canto superior esquerdo da tela. A origem (0, 0) é o canto
    superior esquerdo da tela e a altura e a largura aumentam para baixo e para a direita.

    :param janela: objeto curses.window que representa a tela
    :type janela: curses.window
    :return: uma lista com a altura e a largura da fruta
    :rtype: list
    """
    altura, largura = janela.getmaxyx()
    return [random.randint(1, altura - 2), random.randint(1, largura - 2)]

def selecionar_dificuldade():
    """
    Função que pede ao usuario para escolher a dificuldade do jogo e retorna a velocidade
    correspondente.

    A dificuldade é escolhida pelo usuário representada por um número de 1 a 5,
    em que 1 é a mais lenta e 5 é a mais r pida.

    :return: velocidade do jogo em milissegundos
    :rtype: int
    """
    dificuldades = {'1': 500, '2': 300, '3': 150, '4': 100, '5': 80}
    while True:
        resposta = input('Selecione a dificuldade de 1 (lento) a 5 (rápido): ')
        velocidade = dificuldades.get(resposta)
        if velocidade is not None:
            return velocidade
        print('Opção inválida! Escolha um número de 1 a 5.')

def finalizar_jogo(pontuacao, janela):
    """
    Imprime uma mensagem na tela informando que o jogo foi perdido e
    exibe a pontuação final do usuário. A mensagem é centralizada na
    tela e a tela é atualizada com a mensagem por 3 segundos.

    - `pontuacao` : valor da pontua o que o usu rio conseguiu
    - `janela` : objeto que representa a janela do jogo
    """
    altura, largura = janela.getmaxyx()
    mensagem = f'Você perdeu! Pontuação final: {pontuacao}'
    x = int((largura - len(mensagem)) / 2)
    y = int(altura / 2)
    janela.addstr(y, x, mensagem)
    janela.refresh()
    time.sleep(3)

def direcao_e_oposta(nova_direcao, direcao_atual):
    """
    Verifica se a direção atual e a nova direção são opostas.

    - `nova_direcao` : nova dire o que o usu rio quer mover a cobra
    - `direcao_atual` : dire o atual em que a cobra est  se movendo

    :return: True se as dire es forem opostas e False caso contr rio
    :rtype: bool
    """
    if nova_direcao == curses.KEY_UP and direcao_atual == curses.KEY_DOWN: return True
    if nova_direcao == curses.KEY_DOWN and direcao_atual == curses.KEY_UP: return True
    if nova_direcao == curses.KEY_LEFT and direcao_atual == curses.KEY_RIGHT: return True
    if nova_direcao == curses.KEY_RIGHT and direcao_atual == curses.KEY_LEFT: return True
    return False

def cobra_bateu_borda(cobra, janela):
    """
    Verifica se a cobra bateu na borda da tela.

    - `cobra` : lista de coordenadas que representam a cobra
    - `janela` : objeto que representa a janela do jogo

    :return: True se a cobra bater na borda e False caso contr rio
    :rtype: bool
    """
    cabeça = cobra[0]
    altura, largura = janela.getmaxyx()
    if (cabeça[0] <= 0) or (cabeça[0] >= altura - 1): return True
    if (cabeça[1] <= 0) or (cabeça[1] >= largura - 1): return True
    return False

def cobra_bateu_em_si(cobra):
    """
    Verifica se a cobra bateu em si mesma.

    - `cobra` : lista de coordenadas que representam a cobra

    :return: True se a cobra bater em si mesma e False caso contrário
    :rtype: bool
    """
    cabeça = cobra[0]
    corpo = cobra[1:]
    return cabeça in corpo

def cobra_comeu_fruta(cobra, fruta):
    """
    Verifica se a cobra comeu a fruta.

    - `cobra` : lista de coordenadas que representam a cobra
    - `fruta` : lista com as coordenadas da fruta

    :return: True se a cobra comer a fruta e False caso contrário
    :rtype: bool
    """
    return cobra[0] == fruta

def desenhar_mapa(janela):
    """
    Desenha o mapa do jogo na janela.

    - `janela` : objeto que representa a janela do jogo

    :return: None
    """
    janela.clear()
    janela.border(0)

def desenhar_cobra(cobra, janela):
    """
    Desenha a cobra na janela.

    - `cobra` : lista de coordenadas que representam a cobra
    - `janela` : objeto que representa a janela do jogo

    :return: None
    """
    desenhar_ator(ator=cobra[0], janela=janela, caracter="@")
    for parte_corpo in cobra[1:]:
        desenhar_ator(ator=parte_corpo, janela=janela, caracter="s")

def desenhar_ator(ator, janela, caracter):
    """
    Desenha um ator na janela. O ator representado pelas suas
    coordenadas (altura e largura) e por um caractere que impresso
    na janela.

    - `ator` : lista com as coordenadas do ator
    - `janela` : objeto que representa a janela do jogo
    - `caracter` : caractere que representa o ator na janela

    :return: None
    """
    try:
        janela.addch(ator[0], ator[1], caracter)
    except curses.error:
        pass

def mover_ator(ator, direcao):
    """
    Move o ator na direção especificada.

    - `ator` : lista com as coordenadas do ator
    - `direcao` : direção em que o ator deve ser movido

    :return: None
    """
    match direcao:
        case curses.KEY_UP: ator[0] -= 1
        case curses.KEY_LEFT: ator[1] -= 1
        case curses.KEY_DOWN: ator[0] += 1
        case curses.KEY_RIGHT: ator[1] += 1

if __name__ == '__main__':
    velocidade = selecionar_dificuldade()
    curses.wrapper(ciclo_jogo, velocidade_jogo=velocidade)
    print('Fim do jogo!')