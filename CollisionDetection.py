import pygame
import sys
from pygame.locals import *

from Helpers import * 

class CollisionDetection:
  def __init__(self, obstacles = []):
    self.obstacles = []

    if obstacles != []:
      self.obstacles = obstacles

  def add_obstacle(self, position, size):
    _obstacle = Obstacle(position, size)
    self.obstacles.append(_obstacle)

  def check_collision(self, position, size, movement):
    _result_vector = Vec2(movement.x,movement.y)
    _right_border = position.x + size.width + movement.x
    _left_border = position.x + movement.x
    _top_border = position.y + movement.y
    _bot_border = position.y + size.height + movement.y
    if movement.x > 0:
      for o in self.obstacles:
        if _right_border > o.position.x and _right_border < o.position.x + o.size.width:
          if _top_border < o.position.y + o.size.height and _bot_border > o.position.y:
            _result_vector.x = movement.x - (_right_border - o.position.x )
            
            print "right"
            break
    elif movement.x < 0:
      for o in self.obstacles:
        if _left_border > o.position.x and _left_border < o.position.x + o.size.width:
          if _top_border < o.position.y + o.size.height and _bot_border > o.position.y:
            _result_vector.x = movement.x + (o.position.x + o.size.width - _left_border)
            #print _result_vector.x
            print "left"
            break

    if movement.y > 0:
      for o in self.obstacles:
        if _right_border > o.position.x and _right_border < o.position.x + o.size.width:
          if _top_border < o.position.y + o.size.height and _bot_border > o.position.y:
            _result_vector.y = movement.y - (_bot_border - o.position.y)
            print "bot"
            break
    elif movement.y < 0:
      for o in self.obstacles:
        if _left_border > o.position.x and _left_border < o.position.x + o.size.width:
          if _top_border < o.position.y + o.size.height and _bot_border > o.position.y:
            _result_vector.y = _top_border - o.position.y + o.size.height
            print "top"
            break

    return _result_vector

  def change_position(self, obj, movement):
    #print "called"
    _result_vector = self.check_collision(obj.position, obj.size, movement)
    #print _result_vector.x, _result_vector.y
    obj.position = Vec2(obj.position.x + _result_vector.x, 
                        obj.position.y + _result_vector.y)


    

class Obstacle:
  def __init__(self, position, size):
    self.position = position
    self.size = size


    
