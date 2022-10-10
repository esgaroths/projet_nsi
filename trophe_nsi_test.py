import pygame, sys
from pygame.locals import *


pygame.init()
pygame.key.set_repeat(10)

impact = pygame.font.SysFont('Impact', 60)
little_impact = pygame.font.SysFont('Impact', 30)

#mode, menu = 0, 

mode = [0]

level = ['rien']

texte_niveau = "aucun niveau n'est sélectionné"

#création fenetre
pygame.display.set_caption("Test_Jeux")
fenetre = pygame.display.set_mode((1500, 800), RESIZABLE)
position_fenetre = fenetre.get_rect()



class bouton:
    def __init__(self, hauteur, longueur, x, y, couleur, texte):
        self.hauteur = hauteur
        self.longueur = longueur
        self.x = x
        self.y = y
        self.couleur = couleur
        self.texte = texte
        self.rectangle = pygame.draw.rect(fenetre, self.couleur, (self.x, self.y, self.longueur, self.hauteur))
       
        
    def apparition(self): 
        pygame.draw.rect(fenetre, self.couleur, (self.x, self.y, self.longueur, self.hauteur))
        text = impact.render(self.texte, True, (0,0,0))
        text_rect = text.get_rect(center=(self.x + self.longueur/2, self.y + self.hauteur/2))
        fenetre.blit(text, text_rect)
        
     
def mode_menu():
    fenetre.fill([250, 250, 250])
    bouton_menu = []
    play_button = bouton(170, 300, 24, 24, (50, 100, 200), 'Jouer')
    bouton_menu.append(play_button)
    level_button = bouton(170, 300, 24, 218, (50, 100, 200), 'Niveau')
    bouton_menu.append(level_button)
    help_button = bouton(170, 300, 24, 412, (50, 100, 200), 'Aide')
    bouton_menu.append(help_button)
    leave_button = bouton(170, 300, 24, 606, (50, 100, 200), 'Quitter')
    bouton_menu.append(leave_button)
    
    for boutons in bouton_menu:
        boutons.apparition()
        
    for event in pygame.event.get() :
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                
                if play_button.rectangle.collidepoint(event.pos):
                    print("play")
                    
                if level_button.rectangle.collidepoint(event.pos):
                    print("level")
                    
                if help_button.rectangle.collidepoint(event.pos):
                    print("aide")
                    
                if leave_button.rectangle.collidepoint(event.pos):
                     pygame.display.quit()
                     sys.exit()
                     
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
            
    pygame.display.flip()
        



while True:
    if mode[0] == 0:
        mode_menu()
    
    
