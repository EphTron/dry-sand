import pygame
import sys
from pygame.locals import *

import math

class Player:
  def __init__(self, NAME, IMG_PATH, START_POS_X, START_POS_Y, TRANS_COLOR):
    #setup player
    self.NAME = NAME
    
    self.X = START_POS_X
    self.Y = START_POS_Y

    self.max_speed = 10
    self.current_speed = 0
    self.acceleration = 1

    self.img = pygame.image.load(IMG_PATH).convert()
    self.img.set_colorkey(TRANS_COLOR)
    self.img_width = self.img.get_width()
    self.img_height = self.img.get_height()
    self.state = "stand"

  def get_x(self):
    return self.X

  def move(self, WASD):
    if WASD[0] == 1: # up
      pass
    if WASD[1] == 1: # left
      _speed = self.current_speed
      if _speed > -self.max_speed:
        _speed -= self.acceleration
      self.current_speed = _speed

    if WASD[2] == 1: # down
      pass
    if WASD[3] == 1: # right
      _speed = self.current_speed
      if _speed < self.max_speed:
        _speed += self.acceleration
      self.current_speed = _speed
    if WASD[1] == WASD[3]:
      self.current_speed *= 0.75
      if abs(self.current_speed) < 0.01:
        self.current_speed = 0

    self.X += self.current_speed
    


  def stop(self):
    self.state = "stand"
    
