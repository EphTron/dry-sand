import pygame
import sys
from pygame.locals import *


class Wave:

  def __init__(self, ID, IMG, IMG_WIDTH, PARTS, X, Y):
    self.ID = ID
    self.IMG = IMG
    self.IMG_WIDTH = IMG_WIDTH
    self.PARTS = PARTS
    self.X = X
    self.Y = Y

  def set_x(self, X):
    self.X = X

  def reduce_x(self, PIXEL):
    self.X -= PIXEL
