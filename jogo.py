import pygame
import random

pygame.init()

x = 1280
y = 720
velocidade = 1
velocidade_barreiras = 1
pontos = 5

# Efeito sonoro
pygame.mixer.music.load('efeitos.sonoros/battleThemeA.wav')
pygame.mixer.music.play(-1)

tela = pygame.display.set_mode((x, y))
pygame.display.set_caption("jogo de tiro")

bg = pygame.image.load('cidade.jpg')
bg = pygame.transform.scale(bg, (x, y))
rodando = True

# Carro de Policía
carro = pygame.image.load('carro.png').convert_alpha()
carro = pygame.transform.scale(carro, (150, 150))
carro_colisao = carro.get_rect()

posicao_carro_x = 50
posicao_carro_y = 515

# Obstáculos
barreira = pygame.image.load('barreiras/barreira_00.png').convert_alpha()
barreira = pygame.transform.scale(barreira, (70, 70))
barreira_colisao = barreira.get_rect()

posicao_barreira_x = 1000
posicao_barreira_y = 595

barreira2 = pygame.image.load('barreiras/barreira_01.png').convert_alpha()
barreira2 = pygame.transform.scale(barreira2, (70, 70))
barreira2_colisao = barreira2.get_rect()

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
        posicao_barreira2_x = random.randint(1500, 1700)

    # Colisão
    if carro_colisao.colliderect(barreira_colisao and barreira2_colisao):
        pontos += 1  # Teste. Aqui será o game over
        print(pontos)

    pygame.draw.rect(tela, (255, 0, 0), carro_colisao, -1)
    pygame.draw.rect(tela, (255, 0, 0), barreira_colisao, -1)
    pygame.draw.rect(tela, (255, 0, 0), barreira2_colisao, -1)
    pygame.Rect.update(carro_colisao, posicao_carro_x + 10,
                       posicao_carro_y + 80, 135, 50)
    pygame.Rect.update(barreira_colisao, posicao_barreira_x,
                       posicao_barreira_y, 65, 60)

    barreira_colisao.y = posicao_barreira_y
    barreira_colisao.x = posicao_barreira_x

    barreira2_colisao.y = posicao_barreira2_y
    barreira2_colisao.x = posicao_barreira2_x

    # Velocidade Tela
    x -= 1

    # Imagem
    tela.blit(barreira, (posicao_barreira_x, posicao_barreira_y))
    tela.blit(barreira2, (posicao_barreira2_x, posicao_barreira2_y))
    tela.blit(carro, (posicao_carro_x, posicao_carro_y))

    pygame.display.update()
