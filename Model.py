import pygame
import sys
from pygame.locals import *

from Player import *
from World import *

class Model:
  def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):

  	self.SCREEN_WIDTH = SCREEN_WIDTH
  	self.SCREEN_HEIGHT = SCREEN_HEIGHT

  	#settings
    self.fps = 60
    self.move_speed = 2
    self.island_pos = 0.33

    #environment
    worlds = []
    root_world = World(len(worlds), self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
    worlds.append(rootworld)

    waves = Waves()

