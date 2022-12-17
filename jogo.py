import pygame
import random

pygame.init()

x = 1280
y = 720
velocidade = 1
velocidade_barreiras = 1
velocidade_bandidos = 1

# Efeito sonoro
musicadefundo = pygame.mixer.music.load('efeitos.sonoros/musica_de_fundo.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)

som_tiro = pygame.mixer.Sound('efeitos.sonoros/som_bala.wav')

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
    retorno_bala_x = posicao_carro_x
    retorno_bala_y = posicao_carro_y
    veloc_bala = 0
    return [retorno_bala_x, retorno_bala_y, triggered, veloc_bala]


# Carro de Policía
carro = pygame.image.load('protagonistas/carro.png')
carro = pygame.transform.scale(carro, (150, 150))

posicao_carro_x = 50
posicao_carro_y = 515

# Munição
bala = pygame.image.load('bala/bala.png').convert_alpha()
bala = pygame.transform.scale(bala, (50, 40))
bala = pygame.transform.rotate(bala, -90)


veloc_bala = 0
pos_x_bala = 100
pos_y_bala = 560

triggered = False

# Obstáculos

barreira = pygame.image.load('barreiras/barreira_00.png')
barreira = pygame.transform.scale(barreira, (70, 70))

bandido = pygame.image.load('inimigos/inimigo1.png')
bandido = pygame.transform.scale(bandido, (50, 50))

bandido2 = pygame.image.load('inimigos/inimigo2.png')
bandido2 = pygame.transform.scale(bandido2, (50, 50))

posicao_barreira_x = 1000
posicao_barreira_y = 595

posicao_bandido_x = 1000
posicao_bandido_y = 595

posicao_bandido2_x = 1500
posicao_bandido2_y = 660

barreira2 = pygame.image.load('barreiras/barreira_01.png')
barreira2 = pygame.transform.scale(barreira2, (70, 70))

posicao_barreira2_x = 1500
posicao_barreira2_y = 660

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

    # Obstáculos
    posicao_barreira_x -= velocidade_barreiras
    if (posicao_barreira_x <= -100):
        posicao_barreira_x = random.randint(1200, 1450)

    posicao_barreira2_x -= velocidade_barreiras
    if (posicao_barreira2_x <= -100):
        posicao_barreira2_x = random.randint(1470, 1700)

    posicao_bandido_x -= velocidade_bandidos
    if posicao_bandido_x <= -100:
        posicao_bandido_x = random.randint(1200, 1450)

    posicao_bandido2_x -= velocidade_bandidos
    if posicao_bandido2_x <= -100:
        posicao_bandido2_x = random.randint(1470, 1700)

    # Velocidade Tela
    x -= 1

    # Retorno da bala
    if pos_x_bala == 1300:
        pos_x_bala, pos_y_bala, triggered, veloc_bala = retorno_bala()

    # Imagem

    tela.blit(bala, (pos_x_bala, pos_y_bala))
    tela.blit(carro, (posicao_carro_x, posicao_carro_y))
    tela.blit(barreira, (posicao_barreira_x, posicao_barreira_y))
    tela.blit(barreira2, (posicao_barreira2_x, posicao_barreira2_y))
    tela.blit(bandido, (posicao_bandido_x, posicao_bandido_y))
    tela.blit(bandido2, (posicao_bandido2_x, posicao_bandido2_y))

    pygame.display.update()
