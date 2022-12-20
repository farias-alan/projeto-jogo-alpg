import pygame
import random

pygame.init()

x = 1280
y = 720
velocidade = 1

# Código da pontuação
pontos = -2
font = pygame.font.Font('freesansbold.ttf', 25)
text = font.render("PONTUAÇÃO: " + str(pontos), True, (0, 0, 0))
textRect = text.get_rect()
textRect.center = (640, 20)

# Efeito sonoro
musicadefundo = pygame.mixer.music.load('efeitos.sonoros/musica_de_fundo.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)

som_tiro = pygame.mixer.Sound('efeitos.sonoros/som_bala.wav')

som_grito = pygame.mixer.Sound('efeitos.sonoros/som_grito.wav')

# tela e cenario
tela = pygame.display.set_mode((x, y))
pygame.display.set_caption("jogo de tiro")

bg = pygame.image.load('cenario/cidade.jpg')
bg = pygame.transform.scale(bg, (x, y))
rodando = True

# Função para retorno da bala


def retorno():
    x = 1350
    y = random.randint(1, 640)
    return [x, y]


def retorno_bala():
    triggered = False
    retorno_bala_x = posicao_carro_x + 50
    retorno_bala_y = posicao_carro_y + 50
    veloc_bala = 0
    return [retorno_bala_x, retorno_bala_y, triggered, veloc_bala]


# Carro de Policía
carro = pygame.image.load('protagonistas/carro.png').convert_alpha()
carro = pygame.transform.scale(carro, (150, 150))
carro_colisao = carro.get_rect()

posicao_carro_x = 50
posicao_carro_y = 515

# Munição
bala = pygame.image.load('bala/bala.png').convert_alpha()
bala = pygame.transform.scale(bala, (50, 40))
bala = pygame.transform.rotate(bala, -90)
bala_col = bala.get_rect()

veloc_bala = 0
pos_x_bala = 100
pos_y_bala = 560

triggered = False

# Obstáculos

barreira = pygame.image.load('barreiras/barreira_00.png').convert_alpha()
barreira = pygame.transform.scale(barreira, (70, 70))
barreira_col_01 = barreira.get_rect()
barreira_col_02 = barreira.get_rect()

posicao_barreira_x = 1000
posicao_barreira_y = 595

pos_barreira_x = 1800
pos_barreira_y = 595

barricada = pygame.image.load('barreiras/barreira_01.png').convert_alpha()
barricada = pygame.transform.scale(barricada, (70, 70))
barricada_col_01 = barricada.get_rect()
barricada_col_02 = barricada.get_rect()

posicao_barricada_x = 1300
posicao_barricada_y = 670

pos_barricada_x = 2100
pos_barricada_y = 670

bandido_01 = pygame.image.load('inimigos/inimigo1.png').convert_alpha()
bandido_01 = pygame.transform.scale(bandido_01, (60, 60))
bandido_01_col = bandido_01.get_rect()

pos_bandido_01_x = 1300
pos_bandido_01_y = 580

bandido_02 = pygame.image.load('inimigos/inimigo2.png').convert_alpha()
bandido_02 = pygame.transform.scale(bandido_02, (60, 60))
bandido_02_col = bandido_02.get_rect()

pos_bandido_02_x = 2300
pos_bandido_02_y = 650


while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    # loop da tela
    tela.blit(bg, (0, 0))

    rel_x = x % bg.get_rect().width
    tela.blit(bg, (rel_x - bg.get_rect().width, 0))
    if rel_x < 1280:
        tela.blit(bg, (rel_x, 0))

    # Movimentação Carro
    movimento = pygame.key.get_pressed()
    if movimento[pygame.K_UP] and posicao_carro_y > 510:
        posicao_carro_y -= velocidade
        if not triggered:
            pos_y_bala -= 1

    if movimento[pygame.K_DOWN] and posicao_carro_y < 580:
        posicao_carro_y += velocidade
        if not triggered:
            pos_y_bala += 1

    # Movimentação da Bala
    if movimento[pygame.K_SPACE]:
        triggered = True
        veloc_bala = 2
        som_tiro.play()

    pos_x_bala += veloc_bala

    # Respawn Obstáculos
    posicao_barreira_x -= velocidade
    if posicao_barreira_x <= -50:
        posicao_barreira_x = 1400

    pos_barreira_x -= velocidade
    if pos_barreira_x <= -50:
        pos_barreira_x = 1400

    posicao_barricada_x -= velocidade
    if posicao_barricada_x <= -50:
        posicao_barricada_x = 1400

    pos_barricada_x -= velocidade
    if pos_barricada_x <= -50:
        pos_barricada_x = 1400

    pos_bandido_01_x -= velocidade
    if pos_bandido_01_x <= -100:
        pos_bandido_01_x = 2200

    pos_bandido_02_x -= velocidade
    if pos_bandido_02_x <= -100:
        pos_bandido_02_x = 2500

    if pos_bandido_01_x == pos_barreira_x:
        pos_bandido_01_x = pos_bandido_01_x + 100

    # Colisão Carro com barreira/barricada
    if carro_colisao.colliderect(barreira_col_01) and posicao_barreira_x <= 100:
        rodando = False

    if carro_colisao.colliderect(barreira_col_02) and pos_barreira_x <= 100:
        rodando = False

    if carro_colisao.colliderect(barricada_col_01) and posicao_barricada_x <= 100:
        rodando = False

    if carro_colisao.colliderect(barricada_col_02) and pos_barricada_x <= 100:
        rodando = False

    # Colisão Bala com bandido
    if bala_col.colliderect(bandido_01_col):
        pontos = pontos + 1
        text = font.render("PONTUAÇÃO: " + str(pontos), True, (0, 0, 0))
        pos_bandido_01_x = 2200
        pos_bandido_01_y = 580

    if bala_col.colliderect(bandido_02_col):
        pontos = pontos + 1
        text = font.render("PONTUAÇÃO: " + str(pontos), True, (0, 0, 0))
        pos_bandido_02_x = 2500
        pos_bandido_02_y = 650

    # Caixa de colisão

    # Carro
    pygame.draw.rect(tela, (255, 0, 0), carro_colisao, -1)

    # Barreira
    pygame.draw.rect(tela, (255, 0, 0), barreira_col_01, -1)
    pygame.draw.rect(tela, (255, 0, 0), barreira_col_02, -1)

    # Barricada
    pygame.draw.rect(tela, (255, 0, 0), barricada_col_01, -1)
    pygame.draw.rect(tela, (255, 0, 0), barricada_col_02, -1)

    # Bala
    pygame.draw.rect(tela, (0, 0, 255), bala_col, -1)

    # Bandido
    pygame.draw.rect(tela, (0, 0, 255), bandido_01_col, -1)
    pygame.draw.rect(tela, (0, 0, 255), bandido_02_col, -1)

    # Ajustes de tamanho e posição da caixa
    pygame.Rect.update(carro_colisao, posicao_carro_x + 10,
                       posicao_carro_y + 85, 135, 45)

    pygame.Rect.update(barreira_col_01, posicao_barreira_x,
                       posicao_barreira_y, 65, 60)
    pygame.Rect.update(barreira_col_02, pos_barreira_x, pos_barreira_y, 65, 65)

    pygame.Rect.update(bandido_01_col, pos_bandido_01_x,
                       pos_bandido_01_y, 2, 50)
    pygame.Rect.update(bandido_02_col, pos_bandido_02_x,
                       pos_bandido_01_y, 2, 65)

    pygame.Rect.update(bala_col, pos_x_bala + 35, pos_y_bala + 15, 2, 30)

    barreira_col_01.y = posicao_barreira_y
    barreira_col_01.x = posicao_barreira_x

    barricada_col_01.y = posicao_barricada_y
    barricada_col_01.x = posicao_barricada_x

    barricada_col_02.y = pos_barricada_y
    barricada_col_02.x = pos_barricada_x

    bandido_01_col.x = pos_bandido_01_x
    bandido_01_col.y = pos_bandido_01_y

    bandido_02_col.x = pos_bandido_02_x
    bandido_02_col.y = pos_bandido_02_y

    # Velocidade Tela
    x -= 1

    # Retorno da bala
    if pos_x_bala == 1300:
        pos_x_bala, pos_y_bala, triggered, veloc_bala = retorno_bala()

    # Imagem
    tela.blit(bala, (pos_x_bala, pos_y_bala))

    tela.blit(barreira, (posicao_barreira_x, posicao_barreira_y))
    tela.blit(barreira, (pos_barreira_x, pos_barreira_y))

    tela.blit(barricada, (posicao_barricada_x, posicao_barricada_y))
    tela.blit(barricada, (pos_barricada_x, pos_barricada_y))

    tela.blit(bandido_01, (pos_bandido_01_x, pos_bandido_01_y))
    tela.blit(bandido_02, (pos_bandido_02_x, pos_bandido_02_y))

    tela.blit(carro, (posicao_carro_x, posicao_carro_y))

    tela.blit(text, textRect)

    pygame.display.update()
