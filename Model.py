import pygame
import sys
from pygame.locals import *

from Player import *
from World import *
from Waves import *
from Helpers import * 

import Collision

class Model:
  def __init__(self, SCREEN_SIZE):

    self.SCREEN_SIZE = SCREEN_SIZE
    self.screen = pygame.display.set_mode((SCREEN_SIZE.width, SCREEN_SIZE.height))
    pygame.display.set_caption("dry-sand")

    #settings
    self.fps = 60
    self.move_speed = 2
    self.island_pos = 0.75
    self.world_line_width = 70
    self.trans_color = pygame.Color(255,255,255)

    Collision.detector.add_obstacle(Vec2(600, 700), Size(100, 200))
    world_y = self.SCREEN_SIZE.height * self.island_pos - self.world_line_width
    Collision.detector.add_obstacle( Vec2(0, world_y+15), Size(self.SCREEN_SIZE.width, self.world_line_width))
    
    #init environment
    self.worlds = []
    self.root_world = World(len(self.worlds), self.SCREEN_SIZE, self.world_line_width)
    self.worlds.append(self.root_world)
    self.current_world = self.root_world

    self.waves = Waves(self.island_pos, self.SCREEN_SIZE, self.trans_color)

    #init player
    self.player = Player("Jimmy", "imgs/player.png", Vec2( 20, self.SCREEN_SIZE.height * self.island_pos - 140), self.trans_color)

