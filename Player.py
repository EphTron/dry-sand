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

    self.horizon=START_POS_Y

    self.max_speed = 10
    self.x_current_speed = 0
    self.y_current_speed = 0
    self.x_acceleration = 1
    self.y_acceleration = 1
    self.jump_count = 0.0
    self.jump_power = 20
    self.multi_jump_threshold = 10.0


    self.img = pygame.image.load(IMG_PATH).convert()
    self.img.set_colorkey(TRANS_COLOR)
    self.img_width = self.img.get_width()
    self.img_height = self.img.get_height()
    self.state = "stand"

  def get_x(self):
    return self.X

  def move(self, WASD):
    _speed=self.y_current_speed

    if WASD[0] == 1: # up


      if self.jump_count <= 2: # new jump
        self.jump_count += 1
        print "jump"
        _speed -= self.jump_power/pow(self.jump_count,0.5)# * pow((abs(self.multi_jump_threshold-_speed)*(1/self.multi_jump_threshold)),1.4)

      #if 
    # every frame
    if (self.Y + _speed+self.y_acceleration) < self.horizon:#above ground this frame
      _speed += self.y_acceleration  
      #print "above ground"
    else:
      self.Y=self.horizon
      self.jump_count=0
      _speed=0
      #print "below ground"



    if WASD[2] == 1: # down
      pass

    self.y_current_speed=_speed
    self.Y += self.y_current_speed



    if WASD[1] == 1: # left
      _speed = self.x_current_speed
      if _speed > -self.max_speed:
        _speed -= self.x_acceleration
      self.x_current_speed = _speed

    if WASD[3] == 1: # right
      _speed = self.x_current_speed
      if _speed < self.max_speed:
        _speed += self.x_acceleration
      self.x_current_speed = _speed

    if WASD[1] == WASD[3]: # neither left nor right
      self.x_current_speed *= 0.75
      if abs(self.x_current_speed) < 0.01:
        self.x_current_speed = 0

    self.X += self.x_current_speed
    


  def stop(self):
    self.state = "stand"
    
