import pygame
import sys
from pygame.locals import *


class Wave:

  def __init__(self, ID, IMG, X, Y):
    self.ID = ID
    self.IMG = IMG
    self.X = X
    self.Y = Y

  def move (self):
    print " top"
