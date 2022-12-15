import pygame
pygame.init()

x = 1280
y = 720

screem = pygame.display.set_mode((x,y))
pygame.display.set_caption("jogo de tiro")

bg = pygame.image.load("imagens/imagemcidade.png")
bg = pygame.transform.scale(bg, (x,y))
rodando = True

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.quit:

            rodando = False
    screem.blit(bg, (0,0))

    rel_x = x % bg.get_rect().width
    screem.blit(bg, (rel_x - bg.get_rect().width,0))
    if rel_x < 1280:
        screem.blit(bg,(rel_x, 0))
    
    x -= 1



    pygame.display.update()
