import pygame
import sys
from pygame.locals import *

from Model import *
from View import *
from Controller import *

# setup pygame
pygame.init()

model = Model(800, 600)
view = View(model, model.screen)
controller = Controller(model, view)

fpsTime = pygame.time.Clock()

#setup main loop
while True:
    view.draw()
    for event in pygame.event.get():
        print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsTime.tick(model.fps)
