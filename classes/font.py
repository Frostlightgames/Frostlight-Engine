import os
import pygame
class Font:
    def __init__(self,scale) -> None:
        self.sprites = {}
        self.scale = scale
        self.gap = 1
        for letter in os.listdir(os.path.join("data","sprites","font")):
            if letter.endswith(".png"):
                sprite = None
                if letter == "questtionmark.png":
                    sprite = pygame.image.load(os.path.join("data","sprites","font","questtionmark.png")).convert_alpha()
                else:
                    sprite = pygame.image.load(os.path.join("data","sprites","font",letter)).convert_alpha()
                size = [sprite.get_width(), sprite.get_height()]
                sprite_surf = pygame.Surface(size)
                sprite_surf.blit(sprite,(0,0))
                sprite = pygame.transform.scale(sprite_surf,(size[0]*self.scale,size[1]*self.scale)).convert_alpha()
                sprite.set_colorkey((0,0,0))
                if letter == "questtionmark.png":
                    self.sprites["?"] = sprite
                else:
                    self.sprites[letter.replace(".png","")] = sprite
        
            self.width = list(self.sprites.values())[0].get_width()
            self.height = list(self.sprites.values())[0].get_height()

    def get(self,letter:str):
        return self.sprites[letter]