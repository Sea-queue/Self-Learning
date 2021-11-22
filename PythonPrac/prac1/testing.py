import pygame, sys
#from pygame.locals import*

pygame.init()
SCREENWIDTH = 300
SCREENHEIGHT = 300
bg_color = (100,255,150)
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

pygame.draw.rect(screen, bg_color, (400, 400, 20, 20),0)
screen.fill(bg_color)

pygame.display.update()

# waint until user quits
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
