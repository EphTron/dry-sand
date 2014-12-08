import pygame
import sys
from pygame.locals import *


class Player:
  def __init__(self, NAME, IMG_PATH, WIDTH, HEIGHT, TRANS_COLOR):
    #setup player
    self.NAME = NAME
    self.WIDTH = WIDTH
    self.HEIGHT = HEIGHT
    
	self.pos_x = 10
	self.pos_y = 170
	self.img = pygame.image.load(IMG_PATH).convert()
	self.img.set_colorkey(TRANS_COLOR)

  def ini(self):
      print "moving"
