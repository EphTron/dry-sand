import pygame
import sys
from pygame.locals import *


class Player:
  def __init__(self, NAME, IMG_PATH, START_POS_X, START_POS_Y, TRANS_COLOR):
    #setup player
    self.NAME = NAME
    
    self.X = START_POS_X
    self.Y = START_POS_Y

    self.speed = 5
    self.img = pygame.image.load(IMG_PATH).convert()
    self.img.set_colorkey(TRANS_COLOR)
    self.img_width = self.img.get_width()
    self.img_height = self.img.get_height()
    self.state = "stand"

  def get_x(self):
    return self.X

  def move_right(self):
    self.X += self.speed
    self.state = "right"

  def move_left(self):
    self.X -= self.speed
    self.state = "left"

  def stop(self):
    self.state = "stand"
    
