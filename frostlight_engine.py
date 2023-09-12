import os
import time
import pygame
import argparse
from classes.input import Input
from classes.logger import Logger
from classes.window import Window
from classes.builder import Builder

class Engine:
    def __init__(self,
                 color_depth:int=16,
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
                 window_name:str="New Game",
                 window_size:list=None):
        
        # initialize all modules
        pygame.init()
        pygame.joystick.init()
        if sounds:
            pygame.mixer.pre_init(44100,-16,2,512)

        # Boolean variables go here
        self.run_game = True
        self.sounds = sounds

        # Integer and float variables go here
        self.fps = fps
        self.delta_time = 1
        self.last_time = time.time()
        self.version = 0.1

        # String variables go here
        self.game_state = "intro"
        self.game_version = game_version
        self.language = language

        # List variables go here
        self.display_update_rects = []

        # Object variables go here
        self.clock = pygame.time.Clock()
        self.builder = Builder(self)
        self.logger = Logger(self)
        self.input = Input(self)
        self.window = Window(self,window_size,fullscreen,resizable,nowindow,window_centered,vsync,window_name,mouse_visible,color_depth)

        # Object processing go here
        self.window.create()
        pygame.event.set_allowed([pygame.QUIT, pygame.WINDOWMOVED, pygame.VIDEORESIZE, pygame.KEYDOWN])

    def scale_rect(rect:pygame.Rect, amount:float) -> pygame.Rect:
        w = rect.width * amount
        h = rect.height * amount
        new = pygame.Rect(0,0,w,h)
        return new
    
    def scale_sprite(sprite:pygame.Surface, amount:float) -> pygame.Rect:
        w = sprite.get_width() * amount
        h = sprite.get_height() * amount
        new = pygame.transform.scale(sprite,(w,h)).convert_alpha()
        return new
        
    def get_events(self):
        self.clock.tick(self.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            # Window events
            elif event.type == pygame.WINDOWMOVED:
                self.last_time = time.time()
                self.delta_time = 0

            elif event.type == pygame.VIDEORESIZE:
                if not self.window.fullscreen:
                    self.last_time = time.time()
                    self.delta_time = 0
                    self.window.resize([event.w,event.h])

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    self.window.toggle_fullscreen()

    def engine_update(self):
        self.delta_time = time.time()-self.last_time
        self.last_time = time.time()

    def engine_draw(self):
        pygame.display.update()

    def run(self):
        self.logger.info("Starting game...")
        while self.run_game:
            try:
                self.get_events()
                self.engine_update()
                self.update()
                self.draw()
                self.engine_draw()
            except Exception as e:
                self.logger.error(e)
        self.logger.info("Closed game")

    def quit(self):
        self.run_game = False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pack", action="store_true")
    parser.add_argument("-b", "--build", action="store_true")
    parser.add_argument("-n", "--name", action="store_true")
    args = parser.parse_args()
    if args.pack:

        # Pack Engine for release
        ordner_pfad = "./classes"
        ausgabe_datei = "ausgabe.py"
        main_datei = "frostlight_engine.py"
        imports = []
        # classes ordner durchsuchen und dateien einlesen
        for ordnername, _, dateien in os.walk(ordner_pfad):
            for datei in dateien:
                if datei.endswith(".py"):
                    datei_pfad = os.path.join(ordnername, datei)
                    with open(datei_pfad, "r", encoding="utf-8") as datei_handle:
                        datei_inhalt = datei_handle.read()
                        for zeile in datei_inhalt.split("\n"):
                            if zeile.strip().startswith("import ") or zeile.strip().startswith("from "):
                                if not zeile.strip().startswith("from classes."):
                                    imports.append(zeile.strip())

        imports = sorted(set(imports))
        # main datei einlesen
        with open(main_datei, "r", encoding="utf-8") as main_handle:
            main_inhalt = main_handle.read()

            for zeile in main_inhalt.split("\n"):
                if zeile.strip().startswith("import ") or zeile.strip().startswith("from "):
                    if not zeile.strip().startswith("from classes."):
                        imports.append(zeile.strip())

        imports = sorted(set(imports))
        # ausgabe datei erstellen und schreiben
        with open(ausgabe_datei, "w", encoding="utf-8") as ausgabe_handle:
            for importzeile in imports:
                ausgabe_handle.write(f"{importzeile}\n")
            ausgabe_handle.write("\n") 
            for ordnername, _, dateien in os.walk(ordner_pfad):
                for datei in dateien:
                    if datei.endswith(".py"):
                        datei_pfad = os.path.join(ordnername, datei)
                        with open(datei_pfad, "r", encoding="utf-8") as datei_handle:
                            datei_inhalt = datei_handle.read()
                            for importzeile in imports:
                                datei_inhalt = datei_inhalt.replace(importzeile, "")
                            datei_inhalt = "\n".join(line for line in datei_inhalt.split("\n") if line.strip() and not line.strip().startswith("from classes."))
                            ausgabe_handle.write(datei_inhalt.strip())
                        ausgabe_handle.write("\n\n")

            main_inhalt = "\n".join(line for line in main_inhalt.split("\n") if line.strip() and not line.strip().startswith("from classes.") and not line.strip().startswith("import "))
            ausgabe_handle.write(main_inhalt)
            
    elif args.build:
            
        # Build game to EXE
        pass
        
    elif args.name: 

        # Setup new Project with name
        engine = Engine()
        engine.builder.setup_game(args.name)
    else:

        # Setup new no name Project 
        engine = Engine()
        engine.builder.setup_game()