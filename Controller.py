import pygame
import sys
from pygame.locals import *


class Controller:
  def __init__(self, MODEL, VIEW):
    self.MODEL = MODEL
    self.VIEW = VIEW

  def move(self):
      print "moving"
