import pygame
import sys
from pygame.locals import *

#include own libs
from Model import *
from Controller import *


class View:
  def __init__(self, MODEL, SCREEN):
    self.MODEL = MODEL
    self.SCREEN = SCREEN


  def draw(self):
    self.draw_world(self.MODEL.current_world)
    #self.draw_player(self.)
    self.draw_waves(self.MODEL.waves)


  def draw_world(self, WORLD):
   self.SCREEN.fill(WORLD.background)
   _x = self.MODEL.SCREEN_WIDTH
   _y = self.MODEL.SCREEN_HEIGHT * self.MODEL.island_pos - WORLD.line_width
   pygame.draw.line(self.SCREEN, #screen
                   (200,200,0),  # color
                   (0,_y),       # start pos
                   (_x,_y),      # end pos
                   WORLD.line_width)           # line width



  def draw_waves(self, WAVES):
    #print "drew wave"
    for wave in WAVES.wave_list:
      _x = wave.X
      _y = wave.Y
      for i in range(0,wave.PARTS+1):
        self.SCREEN.blit(wave.IMG, (_x, _y))
        _x += wave.IMG.get_width()