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
position_play = button_play.get_rect()
position_play.topleft = (20, 24)

button_perso = pygame.image.load("button_perso.png").convert_alpha()
position_perso = button_perso.get_rect()
position_perso.topleft = (20, 218)

button_help = pygame.image.load("button_help.png").convert_alpha()
position_help = button_help.get_rect()
position_help.topleft = (20, 412)

button_leave = pygame.image.load("button_leave.png").convert_alpha()
position_leave = button_leave.get_rect()
position_leave.topleft = (20, 606)



#mode, menu = 0
mode = [0]

#detection clic de souris sur l'un des boutons + résultat d'un clic de souris sur un bouton
def clic_bouton_menu():
    for event in pygame.event.get() :
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                if position_play.collidepoint(event.pos):
                    print("play")
                if position_perso.collidepoint(event.pos):
                    print("perso")
                    mode[0] = 2
                if position_help.collidepoint(event.pos):
                    print("aide")
                if position_leave.collidepoint(event.pos):
                     pygame.display.quit()
                     sys.exit()
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()


#afficher menu
def afficher_menu():
    fenetre.fill([250,250,250])
    fenetre.blit(button_play, position_play)
    fenetre.blit(button_perso, position_perso)
    fenetre.blit(button_help, position_help)
    fenetre.blit(button_leave, position_leave)
    pygame.display.flip()

#afficher level
def afficher_level():
    fenetre.fill([0,150,0])
    pygame.display.flip()
    
def clic_bouton_level():
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        
    
while True :
    
    if mode[0] == 0:
        clic_bouton_menu()
        afficher_menu()
        
    if mode[0] == 2:
        afficher_level()
        clic_bouton_level()
        

    
    
    
