import pygame, sys
from pygame.locals import *
import time
from random import *

pygame.init()
pygame.key.set_repeat(10)

impact = pygame.font.SysFont('Impact', 60)

pygame.display.set_caption("Test_Jeux")
fenetre = pygame.display.set_mode((1500, 1000), RESIZABLE)
position_fenetre = fenetre.get_rect()

mode = [1]

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
x_balle = [750, 750]
y_balle = [870]
pas_deplacement = 7 
dx = [3]
dy = [3]
vie = [3]
def le_jeu_lvl1():
    fenetre.fill([250, 250, 250])
    pygame.draw.rect(fenetre, (0, 0, 0), (249, 0, 1, 1000))
    pygame.draw.rect(fenetre, (0, 0, 0), (1215, 0, 1, 1000))
    text = impact.render("vie = ", True, (0,0,0))
    fenetre.blit(text, (50,100))
    text2 = impact.render(str(vie[0]), True, (0,0,0))
    fenetre.blit(text2, (160,100))
    pygame.draw.circle(fenetre,(100, 250, 100),(x_balle[0],y_balle[0]),15)
    
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
        if brique.rectangle.collidepoint(x_balle[0] + 10, y_balle[0]):
            dx[0] = dx[0]
            dy[0] = -dy[0]
            liste_brique.remove(brique)
        elif brique.rectangle.collidepoint(x_balle[0] - 10, y_balle[0]):
            dx[0] = dx[0]
            dy[0] = -dy[0]
            liste_brique.remove(brique)
        elif brique.rectangle.collidepoint(x_balle[0], y_balle[0] + 10):
            dx[0] = dx[0]
            dy[0] = -dy[0]
            liste_brique.remove(brique)
        elif brique.rectangle.collidepoint(x_balle[0], y_balle[0] - 10):
            dx[0] = dx[0]
            dy[0] = -dy[0]
            liste_brique.remove(brique)
    
    if dx[0] < 0:
        if dx[0] > (-0.5):
            dx[0] -= 1
    else:
        if dx[0] < 0.5:
            dx[0] += 1
        
        
    if barre_joueur.collidepoint(x_balle[0] + 10, y_balle[0]):
        if x_balle[0] > x_balle[1]:
            dy[0] = -dy[0]
            dx[0] = (x_balle[0] - x_barre[0]) * 0.01 * dx[0]
        elif x_balle[0] < x_balle[1]:
            dy[0] = -dy[0]
            dx[0] = ((x_barre[0] + 100) - x_balle[0]) * 0.01 * dx[0]
        
        else:
            dy[0] = -dy[0]
            
    elif barre_joueur.collidepoint(x_balle[0] - 10, y_balle[0]):
        if x_balle[0] > x_balle[1]:
            dy[0] = -dy[0]
            dx[0] = (x_balle[0] - x_barre[0]) * 0.01 * dx[0]
        elif x_balle[0] < x_balle[1]:
            dy[0] = -dy[0]
            dx[0] = ((x_barre[0] + 100) - x_balle[0]) * 0.01 * dx[0]
        
        else:
            dy[0] = -dy[0]
    elif barre_joueur.collidepoint(x_balle[0], y_balle[0] + 10):
        if x_balle[0] > x_balle[1]:
            dy[0] = -dy[0]
            dx[0] = (x_balle[0] - x_barre[0]) * 0.01 * dx[0]
        elif x_balle[0] < x_balle[1]:
            dy[0] = -dy[0]
            dx[0] = ((x_barre[0] + 100) - x_balle[0]) * 0.01 * dx[0]
        
        else:
            dy[0] = -dy[0]      
    elif barre_joueur.collidepoint(x_balle[0], y_balle[0] - 10):
        if x_balle[0] > x_balle[1]:
            dy[0] = -dy[0]
            dx[0] = (x_balle[0] - x_barre[0]) * 0.01 * dx[0]
        elif x_balle[0] < x_balle[1]:
            dy[0] = -dy[0]
            dx[0] = ((x_barre[0] + 100) - x_balle[0]) * 0.01 * dx[0]
        
        else:
            dy[0] = -dy[0]
        
        
    x_balle[1] = x_balle[0]
    x_balle[0] += dx[0]
    y_balle[0] -= dy[0]
    
    if y_balle[0] - 18 > 1000:
        x_balle[0] = x_barre[0] + 50
        y_balle[0] = 870
        pygame.draw.circle(fenetre,(100, 250, 100),(x_balle[0],y_balle[0]),15)
        pygame.display.flip()
        vie[0] -= 1
        time.sleep(0.5)
        
    if vie[0] == 0:
        mode[0] = 2
    
    if liste_brique == []:
        mode[0] = 3
        
    
    pygame.display.flip()

def victoire():
    fenetre.fill([0, 0, 0])
    text = impact.render('VICTOIRE', True, (250,250,180))
    fenetre.blit(text, (700, 450))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
            
    pygame.display.flip()
    
def defaite():
    fenetre.fill([0,0,0])
    text = impact.render('DEFAITE', True, (250, 50, 100))
    fenetre.blit(text, (680, 450))
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
    
    pygame.display.flip()
    
while True :
    if mode[0] == 1:
        le_jeu_lvl1()
    if mode[0] == 2:
        defaite()   
    if mode[0] == 3:
        victoire()
    
