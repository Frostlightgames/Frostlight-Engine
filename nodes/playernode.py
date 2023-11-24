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
    def __init__(self, engine, sprite: pygame.Surface, jump_input:str, acc: int = 200, dcc: int = 350, gravity:int=300, ground:int=500, max_speed: int = 1000, max_jump_height: int = 100, jump_strength: int = 200, coyote_time_duration: float = 0.2) -> None:
        super().__init__(engine, sprite, acc, dcc, max_speed)
        self.ground = ground
        self.on_ground = True
        self.gravity = gravity
        self.jump_strength = jump_strength
        self.is_jumping = False
        self.coyote_time = 0.0
        self.coyote_time_duration = coyote_time_duration
        self.jump_pressed = False
        self.max_jump_height = max_jump_height
        self.remaining_jump_height = max_jump_height
        self.jump_input = jump_input

    def update(self):
        self.vel.x += (self.engine.input.get("right")-self.engine.input.get("left"))*self.acc*self.engine.delta_time
        self.vel.x += numpy.sign(self.vel.x) * -1 * self.dcc * self.engine.delta_time * int(not(numpy.sign(self.engine.input.get("right")-self.engine.input.get("left"))))
        self.vel.x = max(min(self.vel.x,self.max_speed),-self.max_speed)
        self.pos.x += self.vel.x * self.engine.delta_time

        # if not self.on_ground:
        #     self.coyote_time += self.engine.delta_time
        # else:
        #     self.coyote_time = 0.0

        self.coyote_time = (self.coyote_time + self.engine.delta_time) * int(not self.on_ground)

        if self.engine.input.get(self.jump_input):
            if (self.on_ground or self.coyote_time < self.coyote_time_duration) and not self.is_jumping and self.remaining_jump_height > 0:
                self.is_jumping = True
                self.jump_pressed = True

        if self.is_jumping:
            self.vel.y = -self.jump_strength
            self.remaining_jump_height -= abs(self.vel.y) * self.engine.delta_time  # Reduziere die verbleibende Sprunghöhe
            if not self.jump_pressed or self.remaining_jump_height <= 0:
                self.is_jumping = False
        
        #if not self.engine.input.get("jump"):
        #    self.jump_pressed = False

        self.jump_pressed = int(self.jump_pressed) * int(self.engine.input.get(self.jump_input))
        
        # Gravity
        self.vel.y += self.gravity * self.engine.delta_time
        self.pos.y += self.vel.y * self.engine.delta_time

        if self.vel.y != 0:
            self.on_ground = False

        # if self.pos.y + self.sprite.get_height() >= self.ground:  # Adjust with player's height
        #     self.pos.y = self.ground - self.sprite.get_height()
        #     self.vel.y = 0
        #     self.on_ground = True
        #     self.is_jumping = False
        #     self.remaining_jump_height = self.max_jump_height

        collision_ground = self.pos.y + self.sprite.get_height() >= self.ground

        self.pos.y = max((self.ground - self.sprite.get_height())*collision_ground,self.pos.y*int(not collision_ground))
        self.vel.y = int(not collision_ground)*self.vel.y
        self.on_ground = max(collision_ground,self.on_ground)
        self.is_jumping = int(not collision_ground)*int(self.is_jumping)
        self.remaining_jump_height = max(self.max_jump_height*collision_ground,self.remaining_jump_height*int(not collision_ground))