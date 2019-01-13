background_img_file="../clipart/bluesea.png"
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen=pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Hello World!")
background_img=pygame.image.load(background_img_file).convert()

while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()

	screen.blit(background_img,(0,0))

	pygame.display.update()

