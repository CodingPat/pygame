import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#taille de la fenêtre
window_width=640
window_height=480

#taille du rectangle
rect_width=600
rect_height=440

#coordonnées du rectangle positionné au centre de la fenêtre
rect_x=20
rect_y=20

#création de la fenêtre
window = pygame.display.set_mode((window_width,window_height))

#boucle principale
while True:
	#boucle de traitement des événements	
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()
	#dessiner le rectangle
	pygame.draw.rect(window,(255,0,0),(rect_x,rect_y,rect_width,rect_height))
	
	#affichage/mise à jour de l'écran
	pygame.display.update()




