import pygame

class Transition:
    def __init__(self,engine) -> None:
        self.engine = engine
        self.surf = pygame.Surface(self.engine.win.get_size())
        self.surf.fill((0,0,0))
        self.size = self.surf.get_size()
        self.alpha = 0
        self.state = 0
        self.speed = 255

    def update(self):
        if self.state == 1:
            self.alpha = min(self.alpha+self.speed*self.engine.delta_time,255)
            if self.alpha == 255:
                self.state = 2
                return True
        if self.state == 2:
            self.alpha = max(self.alpha-self.speed*self.engine.delta_time,0)
            if self.alpha == 0:
                self.state = 0

    def draw(self):
        self.surf.set_alpha(self.alpha)
        self.engine.win.blit(self.surf,(0,0))

    def start(self):
        self.state = 1
        self.alpha = 0