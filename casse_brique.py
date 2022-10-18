import pygame, sys
from pygame.locals import *
import time
from random import *

pygame.init()
pygame.key.set_repeat(10)

pygame.display.set_caption("Test_Jeux")
fenetre = pygame.display.set_mode((1500, 1000), RESIZABLE)
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
    brique = Brique(50, 90, 260 + (x % 10)*95 , 50 + (x // 10)*55, (250, 100, 100))
    liste_brique.append(brique)

x_barre = [700]
y_barre = [900]
x_balle = [750]
y_balle = [890]
pas_deplacement = 7 
dx = [4]
dy = [4]
def le_jeu_lvl1():
    fenetre.fill([250, 250, 250])
    pygame.draw.rect(fenetre, (0, 0, 0), (249, 0, 1, 1000))
    pygame.draw.rect(fenetre, (0, 0, 0), (1215, 0, 1, 1000))
    pygame.draw.circle(fenetre,(100, 250, 100),(x_balle[0],y_balle[0]),10)
    for brique in liste_brique:
        brique.apparition()
        
    barre_joueur = pygame.draw.rect(fenetre, (100, 100, 250), (x_barre[0], y_barre[0], 100, 20)) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_d:
                if x_barre[0] < 1110:
                    x_barre[0] += pas_deplacement
                           
            if event.key == K_q :
                if x_barre[0] > 256:
                    x_barre[0] -= pas_deplacement
                    
    if x_balle[0] >= 1215 or x_balle[0] <= 250:
        dx[0] = -dx[0]
    if y_balle[0] <= 0:
        dy[0] = -dy[0]
        
    for brique in liste_brique:
        if brique.rectangle.collidepoint(x_balle[0], y_balle[0]):
            dx[0] = -dx[0]
            dy[0] = -dy[0]
    if barre_joueur.collidepoint(x_balle[0], y_balle[0]):
        dx[0] = -dx[0]
        dy[0] = -dy[0]
        
    x_balle[0] += dx[0]
    y_balle[0] -= dy[0]
        
    pygame.display.flip()

while True :              
    le_jeu_lvl1()
    
   
     
    
