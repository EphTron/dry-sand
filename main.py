import pygame
import sys
from pygame.locals import *

from Model import *
from View import *
from Controller import *
from Helpers import *

import Collision

# setup pygame
pygame.init()
Collision.init()
#detector = CollisionDetection()

model = Model(Size(1200, 1200))
view = View(model, model.screen)
controller = Controller(model, view)

fpsTime = pygame.time.Clock()

while 1:
  controller.run(fpsTime)