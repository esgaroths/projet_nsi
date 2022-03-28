import pygame, sys
from pygame.locals import *

pygame.init()
pygame.key.set_repeat(10)

impact = pygame.font.SysFont('Impact', 60)
little_impact = pygame.font.SysFont('Impact', 30)

#mode, menu = 0, jeux = 1, choix level = 2, aide = 3, level_math = math, level_physique ) physique etc 

mode = [0]

level = ['rien']

texte_niveau = "aucun niveau n'est sélectionné"

#création fenetre
pygame.display.set_caption("Test_Jeux")
fenetre = pygame.display.set_mode((1500, 800), RESIZABLE)
position_fenetre = fenetre.get_rect()

#MENU

button_play = pygame.draw.rect(fenetre, (0, 100, 255), (20, 24, 300, 170))
text_play = impact.render('Play', True, (0,0,0))

button_level = pygame.draw.rect(fenetre, (0, 100, 255), (20, 218, 300, 170))
text_level = impact.render('Level', True, (0,0,0))


button_help = pygame.draw.rect(fenetre, (0, 100, 255), (20, 412, 300, 170))
text_help = impact.render('Aide', True, (0,0,0))


button_leave = pygame.draw.rect(fenetre, (0, 100, 255), (20, 606, 300, 170))
text_leave = impact.render('Quitter', True, (0,0,0))

text_level_selec = little_impact.render(texte_niveau, True, (0,0,0))


def clic_bouton_menu():
    for event in pygame.event.get() :
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                
                if button_play.collidepoint(event.pos):
                    print("play")
                    
                if button_level.collidepoint(event.pos):
                    print("level")
                    mode[0] = 2
                    
                if button_help.collidepoint(event.pos):
                    print("aide")
                    
                if button_leave.collidepoint(event.pos):
                     pygame.display.quit()
                     sys.exit()
                     
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()


#MENU
def afficher_menu():
    fenetre.fill([250,250,250])
    
    button_level = pygame.draw.rect(fenetre, (0, 100, 255), (20, 218, 300, 170))
    fenetre.blit(text_level, (100, 260))
    
    button_play = pygame.draw.rect(fenetre, (0, 100, 255), (20, 24, 300, 170))
    fenetre.blit(text_play, (100, 66))
    
    button_help = pygame.draw.rect(fenetre, (0, 100, 255), (20, 412, 300, 170))
    fenetre.blit(text_help, (100, 454))
    
    button_leave = pygame.draw.rect(fenetre, (0, 100, 255), (20, 606, 300, 170))
    fenetre.blit(text_leave, (100, 648))
    
    fenetre.blit(text_level_selec, (330, 80))
    
    pygame.display.flip()


#LEVEL
 
button_back = pygame.draw.rect(fenetre, (0, 100, 255), (1230, 24, 250, 135))
text_back = impact.render('Retour', True, (0,0,0))

button_math = pygame.draw.rect(fenetre, (0, 100, 255), (20, 24, 250, 135))
text_math = little_impact.render('Mathémathiques', True, (0,0,0))


def afficher_level():
    fenetre.fill([250,250,250])
    
    button_back = pygame.draw.rect(fenetre, (0, 100, 255), (1230, 24, 250, 135))
    fenetre.blit(text_back, (1276, 55))
    
    button_math = pygame.draw.rect(fenetre, (0, 100, 255), (20, 24, 250, 135))
    fenetre.blit(text_math, (50, 70))
    
    pygame.display.flip()
    
def clic_bouton_level():
    for event in pygame.event.get() :
        
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                
                if button_back.collidepoint(event.pos):
                    mode[0] = 0
                if button_math.collidepoint(event.pos):
                    mode[0] = "math"
                    
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()


#MATH
 
button_trinome = pygame.draw.rect(fenetre, (0, 100, 255), (20, 24, 275, 135))
text_trinome = little_impact.render('Trinome du second degres', True, (0,0,0))

def afficher_MATH():
    fenetre.fill([250,250,250])
    
    button_back = pygame.draw.rect(fenetre, (0, 100, 255), (1230, 24, 250, 135))
    fenetre.blit(text_back, (1276, 55))
    
    button_trinome = pygame.draw.rect(fenetre, (0, 100, 255), (20, 24, 275, 135))
    fenetre.blit(text_trinome, (25, 75))
    pygame.display.flip()
    
def clic_bouton_math():
    for event in pygame.event.get() :
        
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                
                if button_back.collidepoint(event.pos):
                    mode[0] = 2
                
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
        
    if mode[0] == "math":
        afficher_MATH()
        clic_bouton_math()       

    
