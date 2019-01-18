import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#taille de la fenêtre
window_size=(640,480)
wsize_width,wsize_height=window_size

#taille du rectangle
rect_size=(320,240)
rsize_width,rsize_height=rect_size

#coordonnées du rectangle positionné au centre de la fenêtre
rect_x=wsize_width/2-rsize_width/2
rect_y=wsize_height/2-rsize_height/2

#création de la fenêtre
window = pygame.display.set_mode(window_size)

#boucle principale
while True:
	#boucle de traitement des événements	
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()
	#dessiner le rectangle
	pygame.draw.rect(window,(255,0,0),(rect_x,rect_y,rsize_width,rsize_height))
	#dessiner le cercle plein
	pygame.draw.circle(window,(255,255,0),(int(wsize_width/2),int(wsize_height/2)),40,0)
	#dessiner le cercle creux	
	pygame.draw.circle(window,(255,255,0),(int(wsize_width/2),int(wsize_height/2)),80,5)
	#dessiner l'ellipse contenue dans le rectangle 	
	pygame.draw.ellipse(window,(255,255,0),(rect_x,rect_y,rsize_width,rsize_height),5)
	
	#affichage/mise à jour de l'écran
	pygame.display.update()




