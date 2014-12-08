import pygame
import sys
from pygame.locals import *

from Controller import *

# setup pygame
pygame.init()

# globals
FPS  = 60
fpsTime = pygame.time.Clock()
moveSpeed = 3
controller = Controller()

#setup colors
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)

# setup screen
display_w = 800
display_h = 600
setDisplay = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption("hello game")

#setup world
pygame.draw.line(setDisplay, (200,200,0), (0,250),(400,250), 10)

#setup playern
player_pos_x = 10
player_pos_y = 170
player = pygame.image.load('imgs/inselcharakter1.png').convert()
player.set_colorkey(white)
movement = "right"


#setup main loop
while True:
    setDisplay.fill(white)
    pygame.draw.line(setDisplay, (200,200,0), (0,250),(400,250), 10)
    if movement == "left":
        if player_pos_x > 5:
            player_pos_x -= moveSpeed
    elif movement == "right":
        if player_pos_x < 365:
            player_pos_x += moveSpeed
        
    
    setDisplay.blit(player, (player_pos_x,player_pos_y))
    for event in pygame.event.get():
        print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsTime.tick(FPS)
