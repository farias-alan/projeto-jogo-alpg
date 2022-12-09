import pygame

pygame.init()

x = 1280
y = 720

screem = pygame.display.set_mode((x, y))
pygame.display.set_caption("jogo de tiro")

bg = pygame.image.load("imagemcidade.png")
bg = pygame.transform.scale(bg, (x, y))
rodando = True

# Carro de Policía
personagem = pygame.image.load('policia_arma.png')
personagem = pygame.transform.scale(personagem, (150, 150))

posicao_personagem_x = 10
posicao_personagem_y = 500

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            rodando = False
    screem.blit(bg, (0, 0))

    rel_x = x % bg.get_rect().width
    screem.blit(bg, (rel_x - bg.get_rect().width, 0))
    if rel_x < 1280:
        screem.blit(bg, (rel_x, 0))

    x -= 1

    screem.blit(personagem, (posicao_personagem_x, posicao_personagem_y))

    pygame.display.update()

'''
código para movimentação do personagem:

velocidade = 10

   comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT]:
        y += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade
        
'''