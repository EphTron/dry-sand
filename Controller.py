import pygame
import sys
from pygame.locals import *


class Controller:
  def __init__(self, MODEL, VIEW):
    self.MODEL = MODEL
    self.VIEW = VIEW
    self.wasd = [0,0,0,0]
    self.w_has_been_released = True

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
    if _keys[pygame.K_w] and self.w_has_been_released:
      self.wasd[0] = 1
      self.w_has_been_released = False
    else:
      self.wasd[0] = 0

    if _keys[pygame.K_a]:
      self.wasd[1] = 1
    else:
      self.wasd[1] = 0

    if _keys[pygame.K_s]:
      self.wasd[2] = 1
    else:
      self.wasd[2] = 0

    if _keys[pygame.K_d]:
      self.wasd[3] = 1
    else:
      self.wasd[3] = 0

    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      elif (event.type == KEYDOWN):
        if event.key == K_x:
          pygame.quit()
          sys.exit()
      elif event.type == KEYUP:
        if event.key == K_w:
          self.w_has_been_released=True
      #  if event.key == K_a:
      #    self.MODEL.player.stop()

    self.MODEL.player.move(self.wasd) 



