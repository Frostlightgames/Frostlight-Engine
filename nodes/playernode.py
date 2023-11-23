import pygame
import numpy

class PlayerNode():
    def __init__(self,engine,sprite:pygame.Surface,acc:int=400,dcc:int=370,max_speed:int=5000) -> None:
        self.engine = engine
        self.sprite = sprite
        self.pos = pygame.Vector2(0,0)
        self.vel = pygame.Vector2(0,0)
        self.acc = acc
        self.dcc = dcc
        self.max_speed = max_speed

    def update(self):
        pass

    def draw(self):
        self.engine.window.render(self.sprite,self.pos)

class PlayerNodeRPG(PlayerNode):
    def update(self):
        super().update()
        self.vel.x += (self.engine.input.get("right")-self.engine.input.get("left"))*self.acc*self.engine.delta_time
        self.vel.y += (self.engine.input.get("down")-self.engine.input.get("up"))*self.acc*self.engine.delta_time
        
        self.vel.x += numpy.sign(self.vel.x) * -1 * self.dcc * self.engine.delta_time * int(not(numpy.sign(self.engine.input.get("right")-self.engine.input.get("left"))))
        self.vel.y += numpy.sign(self.vel.y) * -1 * self.dcc * self.engine.delta_time * int(not(numpy.sign(self.engine.input.get("down")-self.engine.input.get("up"))))

        self.vel.x = max(min(self.vel.x,self.max_speed),-self.max_speed)
        self.vel.y = max(min(self.vel.y,self.max_speed),-self.max_speed)

        self.pos.x += self.vel.x*self.engine.delta_time
        self.pos.y += self.vel.y*self.engine.delta_time

    def draw(self):
        super().draw()

class PlayerNodePlatformer(PlayerNode):
    def __init__(self, engine, sprite: pygame.Surface, acc: int = 400, dcc: int = 400, g:int=100, horizon:int=720, max_speed: int = 5000) -> None:
        super().__init__(engine, sprite, acc, dcc, max_speed)
        self.horizon = horizon
        self.g = g

    def update(self):
        super().update()
        self.vel.x += (self.engine.input.get("right")-self.engine.input.get("left"))*self.acc*self.engine.delta_time
        self.vel.x += numpy.sign(self.vel.x) * -1 * self.dcc * self.engine.delta_time * int(not(numpy.sign(self.engine.input.get("right")-self.engine.input.get("left"))))
        self.vel.x = max(min(self.vel.x,self.max_speed),-self.max_speed)
        self.pos.x += self.vel.x * self.engine.delta_time

        self.vel.y -= self.engine.input.get("accept") * self.acc * self.engine.delta_time * ()
        self.vel.y += self.g * self.engine.delta_time * int(self.pos.y <= self.horizon) * int(not(self.engine.input.get("accept")))
        self.vel.y = self.vel.y

        self.pos.y += self.vel.y*self.engine.delta_time

    def draw(self):
        super().draw()
    