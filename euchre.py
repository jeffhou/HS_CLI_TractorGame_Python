#Terrain Editor 1.3

#import statements
import pygame,sys,os
from pygame.locals import *
playing_area=pygame.Rect(0,0,183+120,416)
#pygame setup
pygame.init()
screen = pygame.display.set_mode((183+120,256))

card_values=['9','10','j','q','k','a']
card_suits=['c']
card_images={}
#frame setup
for i in card_suits:
	for j in card_values:
		card_images[i+j]=pygame.image.load("img\\"+i+j+'.png')
counter=0
for i in card_suits:
	for j in card_values:
		screen.blit(card_images[i+j],(30*counter,0))
		counter+=1
pygame.display.flip()
