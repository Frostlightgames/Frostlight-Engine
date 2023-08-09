import pygame
class Animation:
    def __init__(self,engine) -> None:
        self.engine = engine
        self.playing_animation = None
        self.animation_time = 0
        self.animation_frame = 0
        self.animations = {
            # name
            # sprites
            # time
            # repeat
        }

    def new(self,name:str,sprites:list,time:int,repeat:bool=True):
        self.animations[name] = {
            "sprites":sprites,
            "time":time,
            "repeat":repeat}
        
    def play(self,name):
        if name in self.animations:
            self.playing_animation = name
            self.animation_time = 0
            self.animation_frame = 0

    def update(self) -> pygame.Surface:
        if self.playing_animation != None:
            self.animation_time += self.engine.delta_time
            if self.animation_time > self.animations[self.playing_animation]["time"]:
                self.animation_time -= self.animations[self.playing_animation]["time"]

            # animation time // max time / animation sprite count
            self.animation_frame = int(divmod(self.animation_time,self.animations[self.playing_animation]["time"]/len(self.animations[self.playing_animation]["sprites"]))[0])
            # cap at max animation frame
            self.animation_frame = max(min(self.animation_frame,len(self.animations[self.playing_animation]["sprites"])-1),0)

            return self.animations[self.playing_animation]["sprites"][self.animation_frame]
