import pygame
from utils import cria_tabuleiro


def inicializa():
    pygame.init()

    # ----- Gera tela principal

    window = pygame.display.set_mode((1024, 720))
    pygame.display.set_caption('Jogo da Barbara')

    estado = {
        "tabuleiro": cria_tabuleiro(2),
        "colorido":True
    }

    return window, estado


def recebe_eventos():
    game = True
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            estado["colorido"] = not estado["colorido"]

    return game


def desenha(window, estado):
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca

    x = 1024/2
    y = 720/2
    raio = 40

    margin = 1.1

    if estado["colorido"]:
        cor_1 = estado['tabuleiro'][0][0]
        cor_2 = estado['tabuleiro'][0][1]
        cor_3 = estado['tabuleiro'][1][0]
        cor_4 = estado['tabuleiro'][1][1]
    else:
        cor_1 = (128, 128, 128)
        cor_2 = (128, 128, 128)
        cor_3 = (128, 128, 128)
        cor_4 = (128, 128, 128)


    cx1 = x - (raio * margin)
    cy1 = y - (raio * margin)
    pygame.draw.circle(window, cor_1, (cx1, cy1), raio)

    cx2 = x + (raio * margin)
    cy2 = y - (raio * margin)
    pygame.draw.circle(window, cor_2, (cx2, cy2), raio)

    cx3 = x - (raio * margin)
    cy3 = y + (raio * margin)
    pygame.draw.circle(window, cor_3, (cx3, cy3), raio)

    cx4 = x + (raio * margin)
    cy4 = y + (raio * margin)
    pygame.draw.circle(window, cor_4, (cx4, cy4), raio)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador


def game_loop(window, estado):

    # ===== Loop principal =====
    while recebe_eventos():
        # ----- Gera saídas
        desenha(window, estado)


janela, estado = inicializa()
game_loop(janela, estado)
