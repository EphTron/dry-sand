import pygame
import sys
from pygame.locals import *

#include own libs
from Model import *
from Controller import *
import Collision

class View:
  def __init__(self, MODEL, SCREEN):
    self.MODEL = MODEL
    self.SCREEN = SCREEN

  def draw(self):
    self.draw_world(self.MODEL.current_world)    
    
    self.draw_waves(self.MODEL.waves)
    self.draw_obstacles()
    self.draw_player(self.MODEL.player)

  def draw_world(self, WORLD):
   self.SCREEN.fill(WORLD.background)
   _x = self.MODEL.SCREEN_SIZE.width
   _y = self.MODEL.SCREEN_SIZE.height * self.MODEL.island_pos - WORLD.line_width
   pygame.draw.line(self.SCREEN,     # screen
                   (200,200,0),      # color
                   (0,_y),           # start pos
                   (_x,_y),          # end pos
                   WORLD.line_width) # line width

  def draw_waves(self, WAVES):
    #print "drew wave"
    for wave in WAVES.wave_list:
      _x = wave.position.x
      _y = wave.position.y
      for i in range(0,wave.PARTS+1):
        self.SCREEN.blit(wave.IMG, (_x, _y))
        _x += wave.IMG.get_width()

  def draw_player(self, PLAYER):
    self.SCREEN.blit(PLAYER.img, (PLAYER.position.x, PLAYER.position.y))

  def draw_obstacles(self):
   for o in Collision.detector.obstacles:
     _x = o.position.x
     _y = o.position.y
     _w = o.size.width
     _h = o.size.height

     pygame.draw.rect(self.SCREEN,     # screen
                     (200,0,0),      # color
                     [_x,_y,_w,_h])