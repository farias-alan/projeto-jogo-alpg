import pygame
import random

pygame.init()

x = 1280
y = 720
velocidade = 1
velocidade_barreiras = 1
velocidade_bandidos = 1


# Código da pontuação
pontos = 0  
font = pygame.font.Font('freesansbold.ttf', 25)
text = font.render("PONTUAÇÃO: " + str(pontos), True, (0, 0, 0))
textRect = text.get_rect()
textRect.center = (640, 20)

# Efeito sonoro
musicadefundo = pygame.mixer.music.load('efeitos.sonoros/musica_de_fundo.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

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
posicao_barricada_y = 660

pos_barricada_x = 2100
pos_barricada_y = 660

bandido = pygame.image.load('inimigos/inimigo1.png').convert_alpha()
bandido = pygame.transform.scale(bandido, (50, 50))

posicao_bandido_x = 1000
posicao_bandido_y = 595

bandido2 = pygame.image.load('inimigos/inimigo2.png').convert_alpha()
bandido2 = pygame.transform.scale(bandido2, (50, 50))

posicao_bandido2_x = 1500
posicao_bandido2_y = 660


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

    posicao_bandido_x -= velocidade
    if posicao_bandido_x <= -100:
        posicao_bandido_x = random.randint(1200, 1450)

    posicao_bandido2_x -= velocidade
    if posicao_bandido2_x <= -100:
        posicao_bandido2_x = random.randint(1470, 1700)

    # Colisão
    if carro_colisao.colliderect(barreira_col_01):
        pontos += 1  # Teste. Aqui será o game over
        print(pontos)

    if carro_colisao.colliderect(barreira_col_02):
        pontos += 1  # Teste. Aqui será o game over
        print(pontos)

    if carro_colisao.colliderect(barricada_col_01):
        pontos += 1  # Teste. Aqui será o game over
        print(pontos)

    if carro_colisao.colliderect(barricada_col_02):
        pontos += 1
        print(pontos)

    pygame.draw.rect(tela, (255, 0, 0), carro_colisao, -1)

    pygame.draw.rect(tela, (255, 0, 0), barreira_col_01, -1)
    pygame.draw.rect(tela, (255, 0, 0), barreira_col_02, -1)

    pygame.draw.rect(tela, (255, 0, 0), barricada_col_01, -1)
    pygame.draw.rect(tela, (255, 0, 0), barricada_col_02, -1)

    pygame.Rect.update(carro_colisao, posicao_carro_x + 10,
                       posicao_carro_y + 80, 135, 50)
    pygame.Rect.update(barreira_col_01, posicao_barreira_x,
                       posicao_barreira_y, 65, 60)
    pygame.Rect.update(barreira_col_02, pos_barreira_x, pos_barreira_y, 65, 65)

    barreira_col_01.y = posicao_barreira_y
    barreira_col_01.x = posicao_barreira_x

    barricada_col_01.y = posicao_barricada_y
    barricada_col_01.x = posicao_barricada_x

    barricada_col_02.y = pos_barricada_y
    barricada_col_02.x = pos_barricada_x

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

    tela.blit(bandido, (posicao_bandido_x, posicao_bandido_y))
    tela.blit(bandido2, (posicao_bandido2_x, posicao_bandido2_y))

    tela.blit(carro, (posicao_carro_x, posicao_carro_y))

    tela.blit(text, textRect)

    pygame.display.update()
