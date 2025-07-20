from __init__ import *
from core.core import Core as _Core
from core.window import *

class FrostlightEngine:
    def __init__(self, fps_limit=0):
        frame = inspect.currentframe()
        if frame is not None:
            args = inspect.getargvalues(frame)[3]
        else:
            args = {}
        self.__core = _Core(args, self.update, self.draw)

        self.window = Window()

    def update(self):
        pass

    def draw(self):
        pass
    
    def run(self):
        self.__core.start_main_loop()

if __name__ == "__main__":
    engine = FrostlightEngine()