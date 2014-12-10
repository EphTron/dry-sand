import pygame
import sys
from pygame.locals import *

#from Player import *
from World import *
from Waves import *

class Model:
  def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):

    self.SCREEN_WIDTH = SCREEN_WIDTH
    self.SCREEN_HEIGHT = SCREEN_HEIGHT
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("dry-sand")

    #settings
    self.fps = 60
    self.move_speed = 2
    self.island_pos = 0.75
    self.trans_color = pygame.Color(255,255,255)

    #environment
    self.worlds = []
    self.root_world = World(len(self.worlds), self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
    self.worlds.append(self.root_world)
    self.current_world = self.root_world

    self.waves = Waves(self.island_pos, self.SCREEN_WIDTH ,self.SCREEN_HEIGHT, self.trans_color)

