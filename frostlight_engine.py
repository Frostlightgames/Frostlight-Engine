import inspect

from init import *

from core.core import Core as _Core
from core.window import Window
from core.sprite import Sprite

class FrostlightEngine:
    def __init__(self, fps_limit=0):
        frame = inspect.currentframe()
        if frame is not None:
            args = inspect.getargvalues(frame)[3]
        else:
            args = {}
        self.__core = _Core(args, self.__engine_update, self.update, self.draw, self.__engine_draw)

        self.window = Window(1920,1080)
        init.WINDOW_CONTEXT = self.window.ctx
        
        self.logger = self.__core.logger
        
        self.delta_time = self.__core.delta_time

    def __engine_update(self):
        self.delta_time = self.__core.delta_time

    def update(self):
        pass

    def draw(self):
        pass
    
    def __engine_draw(self):
        self.window.update()
        self.window.clear()

    def run(self):
        self.__core.start_main_loop()

if __name__ == "__main__":
    engine = FrostlightEngine()