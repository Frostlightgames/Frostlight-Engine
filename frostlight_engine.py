import os
import time
import pygame
import datetime

class Engine:
    def __init__(self,
                 fps:int=0,
                 fullscreen:bool=False,
                 game_version:str="1.0",
                 language:str="en",
                 mouse_visible:bool=True,
                 nowindow:bool=False,
                 resizable:bool=True,
                 sounds:bool=True,
                 vsync:bool=False,
                 window_centered:bool=True,
                 window_depth:int=1,
                 window_name:str="New Game",
                 window_size:list=[1920,1080]):
        
        # initialize all modules
        pygame.init()
        pygame.joystick.init()
        if sounds:
            pygame.mixer.pre_init(44100,-16,2,512)

        # Boolean variables go here
        self.fullscreen = fullscreen
        self.mouse_visible = mouse_visible
        self.nowindow = nowindow
        self.resizable = resizable
        self.run_game = True
        self.sounds = sounds
        self.vsync = vsync
        self.window_centered = window_centered

        # Integer and float variables go here
        self.fps = fps
        self.window_depth = window_depth

        # String variables go here
        self.game_state = "intro"
        self.game_version = game_version
        self.language = language
        self.window_name = window_name

        # List variables go here
        self.window_size = window_size

        # Custom Variables go here

        self.__create_window__()

    def __create_window__(self):
        if not self.nowindow:
            pygame.display.init()
            
            # Center window
            if self.window_centered:
                os.environ['SDL_VIDEO_CENTERED'] = '1'
            else:
                os.environ['SDL_VIDEO_CENTERED'] = '0'

            # Create window
            create_window_size = [int(pygame.display.Info().current_w),int(pygame.display.Info().current_h)]
            if self.fullscreen: # Fullscreen window
                self.win = pygame.display.set_mode(create_window_size,pygame.FULLSCREEN,vsync=self.vsync,depth=self.window_depth)
            else:

                # Calculate fitting window size
                if self.window_size != [1920,1080]:
                    create_window_size = self.window_size
                else:
                    create_window_size = [create_window_size[0],create_window_size[1]*0.94]

                if self.resizable: # Resizable window
                    self.win = pygame.display.set_mode(create_window_size,pygame.RESIZABLE,vsync=self.vsync,depth=self.window_depth)
                else: # Fixed size window
                    self.win = pygame.display.set_mode(create_window_size,vsync=self.vsync,depth=self.window_depth)
            
            # Set window variables
            self.clock = pygame.time.Clock()
            self.win_size = [pygame.display.Info().current_w,int(pygame.display.Info().current_h)]
            
            # Change window attributes
            pygame.display.set_caption(self.window_name)
            pygame.mouse.set_visible(self.mouse_visible)

    def __get_events__(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

    def update(self):
        pass

    def draw(self):
        pass

    def run(self):
        Engine.log("Starting game")
        while self.run_game:
            self.__get_events__()
            self.update()
            self.draw()

    def quit(self):
        self.run_game = False

    def create_file_structure():
        directories_created = 0
        files_created = 0
        directories_to_create = ["data","screenshots",os.path.join("data","classes"),os.path.join("data","sprites")]

        if not os.path.exists(os.path.join("data","log.txt")):
            files_created += 1

        for directory in directories_to_create:
            try:
                os.mkdir(directory)
                directories_created += 1
            except FileExistsError:
                Engine.log(f"Skipping creation of directory {directory}, it already exist.")

        if not os.path.exists("main.py"):
            with open("main.py","+wt") as file:
                file.write("from frostlight_engine import Engine\n")
                file.write("\n")
                file.write("class Game(Engine):\n")
                file.write("    def __init__(self):\n")
                file.write("        super().__init__()\n")
                file.write("\n")
                file.write("    def update(self):\n")
                file.write("        super().update()\n")
                file.write("\n")
                file.write('        if self.gamestate == "intro":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write('        if self.gamestate == "menu":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write('        if self.gamestate == "game":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write('        if self.gamestate == "credits":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write("    def draw(self):\n")
                file.write("        super().draw()\n")
                file.write("\n")
                file.write('        if self.gamestate == "intro":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write('        if self.gamestate == "menu":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write('        if self.gamestate == "game":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write('        if self.gamestate == "credits":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write('if __name__ == "__main__":\n')
                file.write("    game = Game\n")
                file.write("    Game.run()\n")
            files_created += 1
        else:
            Engine.log("Skipping creation of main file, already exist.")

        if files_created == 0 and directories_created == 0:
            Engine.log("No new files and directories where created.")
        else:
            Engine.log(f"Created game files structure with {files_created} files and {directories_created} directories")

    def log(text:str):
        with open(os.path.join("data","log.txt"),"+at") as file:
            if __name__ == "__main__":
                file.write(f"[Engine {datetime.datetime.now()}]: {text} \n")
            else:
                file.write(f"[Game {datetime.datetime.now()}]: {text} \n")
    
    def clear_log():
        with open(os.path.join("data","log.txt"),"w") as file:
            file.write("")

if __name__ == "__main__":
    Engine.create_file_structure()