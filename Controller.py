import pygame
import sys
from pygame.locals import *


class Controller:
  def __init__(self, MODEL, VIEW):
    self.MODEL = MODEL
    self.VIEW = VIEW

  def run(self, time):
    self.get_input()
    self.update_motion()
    self.VIEW.draw() 

    pygame.display.update()
    time.tick(self.MODEL.fps)

  def update_motion(self):
    self.MODEL.waves.update()


  def get_input(self):
    _keys = pygame.key.get_pressed()  #checking pressed keys
    if _keys[pygame.K_a]:
      self.MODEL.player.move_left()
      print("left")
    elif _keys[pygame.K_d]:
      self.MODEL.player.move_right()
      print("right")

    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      elif (event.type == KEYDOWN):
        if event.key == K_x:
          pygame.quit()
          sys.exit()
      elif event.type == KEYUP:
        if event.key == K_d or event.key == K_a:
          self.MODEL.player.stop()      



