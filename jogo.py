import pygame

pygame.init()

x = 1280
y = 720

tela = pygame.display.set_mode((x, y))
pygame.display.set_caption("jogo de tiro")

bg = pygame.image.load("imagemcidade.png")
bg = pygame.transform.scale(bg, (x, y))
rodando = True

# Carro de Policía
carro = pygame.image.load('carro.png')
carro = pygame.transform.scale(carro, (150, 150))

posicao_carro_x = 50
posicao_carro_y = 515

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
        posicao_carro_y -= 1
    if movimento[pygame.K_DOWN] and posicao_carro_y < 580:
        posicao_carro_y += 1

    # Velocidade Tela
    x -= 1

    # Imagem
    tela.blit(carro, (posicao_carro_x, posicao_carro_y))

    pygame.display.update()
