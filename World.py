import pygame
import sys
from pygame.locals import *

import Collision

class World:
  def __init__(self, ID, SIZE, line_width):
    #setup player
    self.ID = ID
    self.SIZE = SIZE

    self.line_width = line_width
    self.left_world = None
    self.right_world = None
    
    self.background = pygame.Color(225,225,255)

  def set_left_world(self, WORLD):
  	self.left_world = WORLD
    
  def set_right_world(self, WORLD):
  	self.right_world = WORLD
    
