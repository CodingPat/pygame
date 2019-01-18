import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#taille de la fenêtre
fenetre_largeur=640
fenetre_hauteur=480

#liste de coordonnees
list_coord=((300,20),(620,460),(20,460))

#création de la fenêtre
fenetre = pygame.display.set_mode((fenetre_largeur,fenetre_hauteur))

#boucle principale
while True:
	#boucle de traitement des événements	
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()
	#affichage du polygone
	pygame.draw.polygon(fenetre,(255,255,0),list_coord,0)


	#affichage/mise à jour de l'écran
	pygame.display.update()




