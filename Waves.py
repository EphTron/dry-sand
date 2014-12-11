import pygame
import sys
from pygame.locals import *

from Wave import *

import random
import math

class Waves:
  def __init__(self, ISLAND_POS, SCREEN_WIDTH, SCREEN_HEIGHT, TRANS_COLOR):

    self.img = pygame.image.load("imgs/wave.png").convert()
    self.img.set_colorkey(TRANS_COLOR)

    self.img_width = self.img.get_width()
    self.img_height = self.img.get_height()

    self.SCREEN_WIDTH = SCREEN_WIDTH

    self.wave_space = SCREEN_HEIGHT * ISLAND_POS
    self.wave_list = []

    self.fill_wave_space()

  def fill_wave_space(self):

    _waves_needed = math.ceil(self.wave_space / (self.img_height * 0.5))
    _parts_needed = 0
    if (self.SCREEN_WIDTH - self.img_width) <= 0:
      _parts_needed = 2
    elif (self.SCREEN_WIDTH - self.img_width) > 0:
      _p = math.ceil(self.SCREEN_WIDTH / self.img_width)
      _parts_needed = _p + 1

    for i in range(0, int(_waves_needed+1)):
      _x = - random.randint(0,self.img_width)
      _y = self.wave_space - self.img_height + (self.img_height* 0.5) * i
      #_img = scale(self.img, (width, height), DestSurface = None)
      _wave = Wave(i, self.img, self.img_width, _parts_needed, _x, _y)
      self.wave_list.append(_wave)

  def update(self):
    for wave in self.wave_list:
      _speed = 0.1 + (wave.ID * 0.08) + random.uniform(0.01,0.05)
      wave.reduce_x(_speed)
      if (wave.X + wave.IMG_WIDTH < 0):
        wave.set_x(0)


