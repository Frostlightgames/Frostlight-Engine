import os
import pygame

class Window:
    def __init__(self,set_window_size=None,fullscreen=False,resizable=True,windowless=False,window_centered=True,vsync=False,window_name="Frostlight Engine",mouse_visible=True,color_depth=24) -> None:
        
        # Setting startup variables
        self.windowless = windowless
        self.window_centered = window_centered
        self.vsync = vsync
        self.color_depth = color_depth
        self.fullscreen = fullscreen
        self.window_name = window_name
        self.mouse_visible = mouse_visible
        self.window_size = set_window_size
        self.resizable = resizable

    def create(self):
        if not self.windowless:
            pygame.display.init()
            
            # Center window
            if self.window_centered:
                os.environ['SDL_VIDEO_CENTERED'] = '1'
            else:
                os.environ['SDL_VIDEO_CENTERED'] = '0'

            # Create window
            display_size = [int(pygame.display.Info().current_w),int(pygame.display.Info().current_h)]
            if self.fullscreen: # Fullscreen window
                self.main_surface = pygame.display.set_mode(display_size,pygame.FULLSCREEN | pygame.DOUBLEBUF,vsync=self.vsync,depth=self.color_depth)
            else:

                # Calculate fitting window size
                if self.window_size == None:
                    self.window_size = [display_size[0],display_size[1]*0.94]

                if self.resizable: # Resizable window
                    self.main_surface = pygame.display.set_mode(self.window_size,pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE,vsync=self.vsync,depth=self.color_depth)
                else: # Fixed size window
                    self.main_surface = pygame.display.set_mode(self.window_size,vsync=self.vsync,depth=self.color_depth)
            
            # Change window attributes
            pygame.display.set_caption(self.window_name)
            pygame.mouse.set_visible(self.mouse_visible)

    def render(self,sprite:pygame.Surface,pos:list[int,int] | pygame.Rect):
        self.main_surface.blit(sprite,pos)

    def resize(self,new_window_size:list):
        
        self.window_size = new_window_size

        if self.resizable:

            # Resizable window 
            self.main_surface = pygame.display.set_mode(self.window_size,pygame.RESIZABLE | pygame.DOUBLEBUF,vsync=self.vsync,depth=self.color_depth)
        else: 
            
            # Fixed size window
            self.main_surface = pygame.display.set_mode(self.window_size,vsync=self.vsync,depth=self.color_depth)

    def set_fullscreen(self,fullscreen:bool):

        # Set fullscreen variable
        self.fullscreen = fullscreen
        pygame.display.quit()
        self.create()

    def toggle_fullscreen(self):

        # Set Fullscreen variable to opposite truth value
        self.set_fullscreen(not(self.fullscreen))

    def set_name(self,name):

        # Renaming the displayed window title
        pygame.display.set_caption(name)

    def get_fps(self,clock):

        # Returning frames per second as integer
        return int(min(clock.get_fps(),99999999))