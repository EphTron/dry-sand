import pygame
import sys
from pygame.locals import *


class World:
  def __init__(self, ID, WIDTH, HEIGHT):
    #setup player
    self.ID = ID
    self.WIDTH = WIDTH
    self.HEIGHT = HEIGHT

    self.line_width = 70
    self.left_world = None
    self.right_world = None
    
    self.background = pygame.Color(225,225,255)

  def set_left_world(self, WORLD):
  	self.left_world = WORLD
    
  def set_right_world(self, WORLD):
  	self.right_world = WORLD
    
