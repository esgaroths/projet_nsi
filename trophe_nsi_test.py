import pygame, sys
from pygame.locals import *

pygame.init()
pygame.key.set_repeat(10)

pygame.display.set_caption("Test_Jeux")
fenetre = pygame.display.set_mode((1500, 900))
position_fenetre = fenetre.get_rect()

button_play = pygame.image.load("button_play.png").convert_alpha()
position_button_play = button_play.get_rect()
position_button_play.center = (750, 450)

while True :
    
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
            

    fenetre.fill([250,250,250])
    fenetre.blit(button_play, position_button_play)
    pygame.display.flip()
    