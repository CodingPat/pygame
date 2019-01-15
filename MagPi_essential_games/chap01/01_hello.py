import pygame
from pygame.locals import *
from sys import exit

pygame.init()

window = pygame.display.set_mode((640,480))

while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()
	pygame.draw.rect(window,(255,0,0),(100,100,50,50))
	pygame.draw.rect(window,(0,255,0),(150,100,50,50))
	pygame.draw.rect(window,(0,0,255),(200,100,50,50))

	pygame.draw.circle(window,(255,255,0),(250,200),20,1)
	
	pygame.display.update()




