import argparse
from __init__ import *

class Engine:
    def __init__(self,
            debug:bool=False,
            fps_limit:int=0,
            game_language:str="en",
            game_version:str="1.0",
            logging:bool=True,
            logging_only_once=True,
            window_mode=None,
            window_aspect_mode=None,
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
            frame = inspect.currentframe()
            ENV.engine = self
            ENV.values = inspect.getargvalues(frame)[3]
        import _core

        self.builder = _core.core.builder
        self.logger = _core.core.logger
        self.save_manager = _core.core.save_manager
        self.window = _core.core.window

        self.game_version = game_version
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
        import _core
        _core.core.loop(self.update,self.draw)

if __name__ == "__main__":

    # Parser arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pack", action="store_true")
    parser.add_argument("-b", "--build", action="store_true")
    args = parser.parse_args()

    if args.pack:

        # Pack Engine for release
        engine = Engine(window_mode=None)

        try:
            engine._core.builder.pack_release()
        except:
            engine.log()

    elif args.build:

        # Build game to EXE
        engine = Engine(window_mode=None)
        try:
            engine.builder.setup_game()
            engine.builder.create_exe()
        except Exception as e:
            engine.logger.log(e)

    else:

        # Setup new no name Project
        engine = Engine(window_mode=None)
        try:
            engine.builder.setup_game()
        except Exception as e:
            engine.logger.log(e)
        