import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#taille de la fenêtre
fenetre_largeur=640
fenetre_hauteur=480

#espace entre les lignes
coordonnee_x1=0
coordonnee_x2=fenetre_largeur
decalage=20

#création de la fenêtre
fenetre = pygame.display.set_mode((fenetre_largeur,fenetre_hauteur))

#boucle principale
while True:
	#boucle de traitement des événements	
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()
	#boucle pour dessiner des rayons
	while((coordonnee_x1 < fenetre_largeur) and (coordonnee_x2 > 0)):
		pygame.draw.line(fenetre,(255,0,0),(coordonnee_x1,0),(coordonnee_x2,fenetre_hauteur),2)
		coordonnee_x1+=decalage
		coordonnee_x2-=decalage
	#affichage/mise à jour de l'écran
	pygame.display.update()




