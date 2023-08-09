from frostlight_engine import *

class Game(Engine):
    def __init__(self):
        super().__init__()
        self.sprite = pygame.image.load("test.jpg").convert()
        self.sprite = pygame.transform.scale(self.sprite,(1920*10,1080*10))

    def update(self):
        self.window.set_name(str(self.window.get_fps(self.clock)))
        if self.game_state == "intro":
            pass

        if self.game_state == "menu":
            pass

        if self.game_state == "game":
            pass

        if self.game_state == "credits":
            pass

    def draw(self):
        self.window.main_surface.blit(self.sprite,(0,0),pygame.Rect(0,0,1920,1080))
        if self.game_state == "intro":
            pass

        if self.game_state == "menu":
            pass

        if self.game_state == "game":
            pass

        if self.game_state == "credits":
            pass
        
        pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()
