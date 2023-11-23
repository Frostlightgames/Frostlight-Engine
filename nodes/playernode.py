import pygame
import numpy
from frostlight_engine import Engine

class PlayerNode():
    def __init__(self) -> None:
        pass

class PlayerNodeRPG(PlayerNode):
    def __init__(self,engine:Engine,sprite:pygame.Surface,acc:int=400,dcc:int=300,max_speed:int=5000):
        self.engine = engine
        self.sprite = sprite
        self.pos = pygame.Vector2(0,0)
        self.vel = pygame.Vector2(0,0)
        self.acc = acc
        self.dcc = dcc
        self.max_speed = max_speed
        
    def update(self):
        self.vel[0] += (self.engine.input.get("right")-self.engine.input.get("left"))*self.acc*self.engine.delta_time
        self.vel[1] += (self.engine.input.get("down")-self.engine.input.get("up"))*self.acc*self.engine.delta_time
        
        self.vel[0] += numpy.sign(self.vel[0]) * -1 * self.dcc * self.engine.delta_time * int(not(numpy.sign(self.engine.input.get("right")-self.engine.input.get("left"))))
        self.vel[1] += numpy.sign(self.vel[1]) * -1 * self.dcc * self.engine.delta_time * int(not(numpy.sign(self.engine.input.get("down")-self.engine.input.get("up"))))

        self.vel[0] = max(min(self.vel[0],self.max_speed),-self.max_speed)
        self.vel[1] = max(min(self.vel[1],self.max_speed),-self.max_speed)

        self.pos.x += self.vel[0]*self.engine.delta_time
        self.pos.y += self.vel[1]*self.engine.delta_time

    def draw(self):
        self.engine.window.render(self.sprite,self.pos)