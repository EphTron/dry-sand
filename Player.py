import pygame
import sys
from pygame.locals import *


class Player:
  def __init__(self, NAME, IMG_PATH, START_POS_X, START_POS_Y, TRANS_COLOR):
    #setup player
    self.NAME = NAME
    
    self.X = START_POS_X
    self.Y = START_POS_Y
    self.img = pygame.image.load(IMG_PATH).convert()
    self.img.set_colorkey(TRANS_COLOR)
    self.img_width = self.img.get_width()
    self.img_height = self.img.get_height()
    self.direction = "right"

  def get_x(self):
    return self.X

  def move_right(self, MOVE):
    self.X += MOVE
    self.direction = "right"

  def move_left(self, MOVE):
    self.X -= MOVE
    self.direction = "left"






"""
# globals
FPS  = 60
fpsTime = pygame.time.Clock()
moveSpeed = 3
controller = Controller()

#setup colors
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)

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
"""