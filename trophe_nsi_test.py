import pygame, sys
from pygame.locals import *

pygame.init()
pygame.key.set_repeat(10)

#création fenetre
pygame.display.set_caption("Test_Jeux")
fenetre = pygame.display.set_mode((1500, 800), RESIZABLE)
position_fenetre = fenetre.get_rect()

#création boutons menu
button_play = pygame.image.load("button_play.png").convert_alpha()
button_perso = pygame.image.load("button_perso.png").convert_alpha()
button_help = pygame.image.load("button_help.png").convert_alpha()
button_leave = pygame.image.load("button_leave.png").convert_alpha()

#detection clic de souris sur l'un des boutons
#résultat d'un clic de souris sur un bouton

while True :
    
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
            

    fenetre.fill([250,250,250])
    fenetre.blit(button_play, (20, 24))
    fenetre.blit(button_perso, (20, 218))
    fenetre.blit(button_help, (20, 412))
    fenetre.blit(button_leave, (20, 606))
    pygame.display.flip()
    