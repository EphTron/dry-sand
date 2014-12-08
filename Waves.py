import pygame
import sys
from pygame.locals import *


class Waves:
  def __init__(self, IMG_PATH, ISLAND_POS, HEIGHT):
    #s
    
    self.img = pygame.image.load(IMG_PATH).convert()
    self.img.set_colorkey(TRANS_COLOR)
    self.

    self.pos_y = 
