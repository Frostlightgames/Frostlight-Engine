from __init__ import *

import os
import _core
from _core import dispatch
from _core.logger import _LogType
import argparse

class Engine:
    def __init__(self,
            debug:bool=False,
            fps_limit:int=0,
            game_language:str="en",
            game_version:str="1.0",
            logging:bool=True,
            logging_only_once=True,
            window_mode=WINDOWED,
            window_aspect_mode=KEEP,
            window_size=None,
            window_centered=True,
            mouse_visible=True,
            window_name="",
            window_icon_path="",
            window_position=[0,0],
            window_color_depth=16,
            vsync = True,
            save_manager_path="data/saves/save") -> None:
        
        if ENV.engine == None:
            ENV.engine = self
        
        self._core = _core.Core(
            debug,
            fps_limit,
            game_language,
            game_version,
            logging,
            logging_only_once,
            window_mode,
            window_aspect_mode,
            window_size,
            window_centered,
            mouse_visible,
            window_name,
            window_icon_path,
            window_position,
            window_color_depth,
            vsync,
            save_manager_path)

        self.window = self._core.window

        self.game_version = game_version

        self.game_state = ""

    @dispatch(str)
    def log(self,message:str):
        self._core.logger.log(message)

    @dispatch(_LogType,Exception)
    def log(self,LogType:_LogType,message:Exception):
        self._core.logger.log(LogType,message)

    @dispatch(_LogType,str)
    def log(self,LogType:_LogType,message:str):
        self._core.logger.log(LogType,message)

    @dispatch()
    def log(self):
        self._core.logger.log()
    
    @dispatch()
    def swich_logging(self):
        self._core.logger.swich_logging()
    
    @dispatch(bool)
    def swich_logging(self,logging:bool):
        self._core.logger.swich_logging(logging)

    def save(self,key,value) -> bool:
        self._core.save_manager.save(key,value)

    def load(self,key,default=None) -> any:
        self._core.save_manager.load(key,default)

    def backup(self,backup_path:str="default",backup_info:dict={}):
            info = {"Game Version":self.game_version,
                    "Window Name":self.window.name}
            info.update(backup_info)
            self._core.save_manager.backup(backup_path,info)

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

if __name__ == "__main__":

    # Parser arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pack", action="store_true")
    parser.add_argument("-b", "--build", action="store_true")
    args = parser.parse_args()

    if args.pack:

        # Pack Engine for release
        engine = Engine(window_mode=HIDDEN)

        try:
            engine._core.builder.pack_release()
        except:
            engine.log()

    elif args.build:

        # Build game to EXE
        engine = Engine(window_mode=HIDDEN)
        try:
            engine._core.builder.setup_game()
            engine._core.builder.create_exe()
        except:
            engine.log()

    else:

        # Setup new no name Project
        engine = Engine(window_mode=HIDDEN)
        try:
            engine._core.builder.setup_game()
        except:
            engine.log()
        