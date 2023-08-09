from frostlight_engine import *

class Game(Engine):
    def __init__(self):
        super().__init__()
    def update(self):
        if self.game_state == "intro":
            pass

        if self.game_state == "menu":
            pass

        if self.game_state == "game":
            pass

        if self.game_state == "credits":
            pass

    def draw(self):
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
