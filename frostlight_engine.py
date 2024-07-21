from __init__ import *

import _core
import _nodes

class Engine:
    def __init__(self,
            debug:bool=False,
            fps_limit:int=0,
            game_language:str="en",
            game_version:str="1.0",
            logging:bool=True,
            logging_only_once=True,
            mouse_visible:bool=True,
            vsync:bool=False,
            window_centered:bool=True,
            window_color_depth:int=16,
            window_fullscreen:bool=False,
            window_icon_path:str="",
            window_name:str="New Game",
            window_resizable:bool=True,
            window_size:list=None) -> None:
        
        if ENV.engine == None:
            ENV.engine = self
        
        self._core = _core.Core()
        self.nodes = _nodes

        self.game_state = ""

    def update(self):
        pass

    def draw(self):
        pass

    def test(self):
        # TODO
        # sys log mit infos über engine z.b. engine_version, game_version 
        print("Test")

    def run(self):
        self._core.loop(self.update,self.draw)