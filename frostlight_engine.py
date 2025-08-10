from __init__ import *
import __init__ as init
from core.core import Core as _Core
from core.window import *
from core.sprite import *

class FrostlightEngine:
    def __init__(self, 
            fps_limit = 0,
            catch_errors = True,
            logging = True,
            one_log_file = False,
            window_mode = None):
        frame = inspect.currentframe()
        if frame is not None:
            args = inspect.getargvalues(frame)[3]
        else:
            args = {}
        self.__core = _Core(args, self.__engine_update, self.update, self.draw, self.__engine_draw)

        self.window = Window()
        init.WINDOW_CONTEXT = self.window.ctx

    def __engine_update(self):
        pass

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