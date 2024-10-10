
import pygame
from utils import cria_tabuleiro


def inicializa():
    pygame.init()

    # ----- Gera tela principal

    window = pygame.display.set_mode((1024, 720))
    pygame.display.set_caption('Jogo da Barbara')

    estado = {
        "tabuleiro": cria_tabuleiro(4),
        "colorido": True
    }
    raio = 40
    diametro = raio * 2
    largura_mapa = diametro * len(estado["tabuleiro"])

    x_canto = (1024 // 2) - (largura_mapa//2)
    y_canto = (720 // 2) - (largura_mapa//2)

    x_c1 = x_canto + raio
    y_c1 = y_canto + raio
    lista_tabuleiro = []

    for i in range(len(estado["tabuleiro"])):
        listinha = []
        for j in range(len(estado["tabuleiro"])):
            x = (i * diametro * 1.05) + x_c1
            y = (j * diametro * 1.05) + y_c1
            listinha.append([x, y])
        lista_tabuleiro.append(listinha)

    estado["centros"] = lista_tabuleiro

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

    if estado["colorido"]:
        for i in range(len(estado["centros"])):
            for j in range(len(estado["centros"])):

                x, y = estado["centros"][i][j]
                cor = estado["tabuleiro"][i][j]
                pygame.draw.circle(window, cor, (x, y), 40)
    else:
        for i in range(len(estado["centros"])):
            for j in range(len(estado["centros"])):

                x, y = estado["centros"][i][j]
                cor = (100, 100, 100)
                pygame.draw.circle(window, cor, (x, y), 40)
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador


def game_loop(window, estado):

    # ===== Loop principal =====
    while recebe_eventos():
        # ----- Gera saídas
        desenha(window, estado)


janela, estado = inicializa()
game_loop(janela, estado)
