import pygame
import sys
from pygame.locals import *

from Wave import *

class Waves:
  def __init__(self, ISLAND_POS, HEIGHT, TRANS_COLOR):

    self.img = pygame.image.load("imgs/waves.png").convert()
    self.img.set_colorkey(TRANS_COLOR)

    self.img_width = self.img.get_width()
    self.img_height = self.img.get_height()

    self.wave_space = HEIGHT * ISLAND_POS
    self.wave_list = []

    self.fill_wave_space()

  def fill_wave_space(self):
    _waves_needed = self.wave_space / (self.img_height * 0.5)
    print "creating wave"
    for i in range(0, int(_waves_needed)):
      _x = -(self.img_width / _waves_needed) * i
      _y = self.wave_space - self.img_height * 0.26 + (self.img_height* 0.5) * i
      _wave = Wave(i,self.img,_x, _y)

      self.wave_list.append(_wave)
      print "created wave:"
      print _x


