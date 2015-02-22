import pygame
import sys
from pygame.locals import *


class Wave:

  def __init__(self, ID, IMG, IMG_WIDTH, PARTS, POSITION):
    self.ID = ID
    self.IMG = IMG
    self.IMG_WIDTH = IMG_WIDTH
    self.PARTS = PARTS
    self.position = POSITION

  def set_x(self, X):
    self.position.x = X

  def reduce_x(self, PIXEL):
    self.position.x -= PIXEL
