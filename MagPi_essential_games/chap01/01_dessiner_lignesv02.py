import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#taille de la fenêtre
fenetre_largeur=640
fenetre_hauteur=480

#espace entre les lignes
coordonnee_y=10
espacement=20

#création de la fenêtre
fenetre = pygame.display.set_mode((fenetre_largeur,fenetre_hauteur))

#boucle principale
while True:
	#boucle de traitement des événements	
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()
	#boucle pour dessiner des lignes parallèles
	while(coordonnee_y < fenetre_hauteur):
		pygame.draw.line(fenetre,(255,0,0),(0,coordonnee_y),(640,coordonnee_y),2)
		coordonnee_y+=espacement
	#affichage/mise à jour de l'écran
	pygame.display.update()




