import pygame, sys
from pygame.locals import *
import time
from random import *

pygame.init()
pygame.key.set_repeat(10)

pygame.display.set_caption("Test_Jeux")
fenetre = pygame.display.set_mode((1500, 900))
position_fenetre = fenetre.get_rect()
        
perso = pygame.image.load("balle_rouge.png").convert_alpha()
position_perso = perso.get_rect()
position_perso.center = (750, 450)

bad = pygame.image.load("bad.png").convert_alpha()
position_bad = bad.get_rect()

bad2 = pygame.image.load("bad.png").convert_alpha()
position_bad2 = bad2.get_rect()
position_bad2.topleft = (1430, 0)

bad3 = pygame.image.load("bad.png").convert_alpha()
position_bad3 = bad3.get_rect()
position_bad3.topleft = (750, 0)

masque_bad = pygame.mask.from_surface(bad)
masque_bad2 = pygame.mask.from_surface(bad2)
masque_bad3 = pygame.mask.from_surface(bad3)
masque_perso = pygame.mask.from_surface(perso)

font = pygame.font.Font(pygame.font.get_default_font(), 36)
texte = font.render("Game Over", True, (255, 0, 0))
position_texte = texte.get_rect()
position_texte.center = position_fenetre.center

pas_deplacement = 6 
vitessebad3 = 2

topchrono = time.time()
delai = 3
delai2 = 6
delai3 = 9
delai4 = 12
delai5 = 15

while True :
    while masque_perso.overlap(masque_bad, (position_bad.left - position_perso.left, position_bad.top - position_perso.top)) == None and masque_perso.overlap(masque_bad2, (position_bad2.left - position_perso.left, position_bad2.top - position_perso.top)) == None and masque_perso.overlap(masque_bad3, (position_bad3.left - position_perso.left, position_bad3.top - position_perso.top)) == None:
    
        lst_coordone_perso = list(position_perso)
        lst_coordone_bad = list(position_bad)
        lst_coordone_bad2 = list(position_bad2)
        lst_coordone_bad3 = list(position_bad3)

        for event in pygame.event.get() :    
            if event.type == KEYDOWN:

                if event.key == K_s :
                    if lst_coordone_perso[1] < 870:
                        position_perso = position_perso.move(0,pas_deplacement)
                        
                if event.key == K_z :
                    if lst_coordone_perso[1] > -30:
                        position_perso = position_perso.move(0,-pas_deplacement)   

                if event.key == K_d :
                    if lst_coordone_perso[0] < 1470:
                        position_perso = position_perso.move(pas_deplacement,0)
                       
                if event.key == K_q :
                    if lst_coordone_perso[0] > -30:
                        position_perso = position_perso.move(-pas_deplacement,0)
                       
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()        
        
        time.sleep(0.006)
        position_bad = position_bad.move(0, pas_deplacement)
        if lst_coordone_bad[1] > 870:
            for i in range(180):
                position_bad = position_bad.move(0, -pas_deplacement)
        position_bad = position_bad.move(pas_deplacement, 0)
        if lst_coordone_bad[0] > 1470:
            for i in range(300):
                position_bad = position_bad.move(-pas_deplacement, 0)
                
        if time.time() - topchrono > delai:
            position_bad2 = position_bad2.move(0, pas_deplacement)
            if lst_coordone_bad2[1] > 870:
                for i in range(180):
                    position_bad2= position_bad2.move(0, -pas_deplacement)
            position_bad2 = position_bad2.move(-pas_deplacement, 0)
            if lst_coordone_bad2[0] < 30:
                for i in range(300):
                    position_bad2 = position_bad2.move(pas_deplacement, 0)
                    
        if time.time() - topchrono > delai2:
            if lst_coordone_bad3[0] > lst_coordone_perso[0]:
                position_bad3 = position_bad3.move(-vitessebad3, 0)
            else:
                position_bad3 = position_bad3.move(vitessebad3, 0)
            if lst_coordone_bad3[1] > lst_coordone_perso[1]:
                position_bad3 = position_bad3.move(0, -vitessebad3)
            else:
                position_bad3 = position_bad3.move(0, vitessebad3)
            
        fenetre.fill([250,250,250])
        fenetre.blit(perso, position_perso)
        fenetre.blit(bad, position_bad)
        if time.time() - topchrono > delai:
            fenetre.blit(bad2, position_bad2)
        if time.time() - topchrono > delai2:
            fenetre.blit(bad3, position_bad3)
        if time.time() - topchrono > delai3:
            vitessebad3 = 3
        if time.time() - topchrono > delai4:
            vitessebad3 = 4
        if time.time() - topchrono > delai5:
            vitessebad3 = 5     
            
        pygame.display.flip()      
     
    for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()                
                
    fenetre.fill([250,250,250])   
    fenetre.blit(texte, position_texte)
    pygame.display.flip()
    
    
        