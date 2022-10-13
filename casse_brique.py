import pygame, sys
from pygame.locals import *
import time
from random import *

pygame.init()
pygame.key.set_repeat(10)

pygame.display.set_caption("Test_Jeux")
fenetre = pygame.display.set_mode((1500, 800), RESIZABLE)
position_fenetre = fenetre.get_rect()

class Brique:
    def __init__(self, hauteur, longueur, x, y, couleur):
        self.hauteur = hauteur
        self.longueur = longueur
        self.x = x
        self.y = y
        self.couleur = couleur
        self.rectangle = pygame.draw.rect(fenetre, self.couleur, (self.x, self.y, self.longueur, self.hauteur))
       
        
    def apparition(self): 
        pygame.draw.rect(fenetre, self.couleur, (self.x, self.y, self.longueur, self.hauteur), )
        
        
liste_brique = []
for x in range(60):
    brique = Brique(50, 140, 5 + (x % 10)*150 , (x // 10)*55, (250, 100, 100))
    liste_brique.append(brique)



x_barre = 700
y_barre = 765
pas_deplacement = 5 


def le_jeu_lvl1():
    fenetre.fill([250, 250, 250])
    for brique in liste_brique:
        brique.apparition()
        
    barre_joueur = pygame.draw.rect(fenetre, (100, 100, 250), (x_barre, y_barre, 100, 20)) 
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        
        if event.key == K_d:
            if x_barre < 1400:
                x_barre += pas_deplacement
                       
        if event.key == K_q :
            if x_barre > 100:
                x_barre -= pas_deplacement
        
        
    pygame.display.flip()

        
    
        
        
    

while True :              
    le_jeu_lvl1()
    
   
     
    