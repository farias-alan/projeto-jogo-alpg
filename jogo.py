import pygame
import random

pygame.init()

x = 1280
y = 720
velocidade = 1
velocidade_barreiras = 1

#Efeito sonoro
pygame.mixer.music.load('efeitos.sonoros/battleThemeA.wav')
pygame.mixer.music.play(-1)


tela = pygame.display.set_mode((x, y))
pygame.display.set_caption("jogo de tiro")

bg = pygame.image.load('cidade.jpg')
bg = pygame.transform.scale(bg, (x, y))
rodando = True

# Carro de Policía
carro = pygame.image.load('carro.png')
carro = pygame.transform.scale(carro, (150, 150))

posicao_carro_x = 50
posicao_carro_y = 515

# Obstáculos

barreira = pygame.image.load('barreiras/barreira_00.png')
barreira = pygame.transform.scale(barreira, (70, 70))

posicao_barreira_x = 1000
posicao_barreira_y = 595

barreira2 = pygame.image.load('barreiras/barreira_01.png')
barreira2 = pygame.transform.scale(barreira2, (70, 70))

posicao_barreira2_x = 1500
posicao_barreira2_y = 660

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    tela.blit(bg, (0, 0))

    rel_x = x % bg.get_rect().width
    tela.blit(bg, (rel_x - bg.get_rect().width, 0))
    if rel_x < 1280:
        tela.blit(bg, (rel_x, 0))

    # Movimentação Carro
    movimento = pygame.key.get_pressed()
    if movimento[pygame.K_UP] and posicao_carro_y > 510:
        posicao_carro_y -= velocidade
    if movimento[pygame.K_DOWN] and posicao_carro_y < 580:
        posicao_carro_y += velocidade

    # Obstáculos
    posicao_barreira_x -= velocidade_barreiras
    if (posicao_barreira_x <= -100):
        posicao_barreira_x = random.randint(1200, 1450)

    posicao_barreira2_x -= velocidade_barreiras
    if (posicao_barreira2_x <= -100):
        posicao_barreira2_x = random.randint(1470, 1700)

    # Velocidade Tela
    x -= 1

    # Imagem
    tela.blit(carro, (posicao_carro_x, posicao_carro_y))
    tela.blit(barreira, (posicao_barreira_x, posicao_barreira_y))
    tela.blit(barreira2, (posicao_barreira2_x, posicao_barreira2_y))

    pygame.display.update()
