import pygame
import sys
from pygame.locals import *

from Model import *
from View import *
from Controller import *

# setup pygame
pygame.init()

model = Model(600, 400)
view = View(model, model.screen)
controller = Controller(model, view)

fpsTime = pygame.time.Clock()

while 1:
  controller.run(fpsTime)