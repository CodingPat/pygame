import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#taille de la fenêtre
window_width=640
window_height=480

#création de la fenêtre
window = pygame.display.set_mode((window_width,window_height))

#boucle principale
while True:
	#boucle de traitement des événements	
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()
	#dessiner une ligne au milieu
	pygame.draw.line(window,(255,0,0),(0,240),(640,240),2)
	
	#affichage/mise à jour de l'écran
	pygame.display.update()




