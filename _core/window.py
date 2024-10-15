import os
import pygame
import pygame._sdl2.video

pygame.display.init()

class WindowMode:
    def __init__(self,type:int) -> None:
        self.type = type

class AspectRatioMode:
    def __init__(self,type:int) -> None:
        self.type = type

WINDOWED = WindowMode(0)
FULLSCREEN = WindowMode(1)
WINDOWED_FULLSCREEN = WindowMode(2)
FRAMELESS = WindowMode(3)
FIXED = WindowMode(4)
HIDDEN = WindowMode(5)

KEEP = AspectRatioMode(0)
SCALE = AspectRatioMode(1)
FREE = AspectRatioMode(2)

class Window:
    def __init__(self,
                 window_mode=WINDOWED,
                 aspect_mode=KEEP,
                 window_size=None,
                 centered=True,
                 mouse_visible=True,
                 window_name="",
                 icon_path="",
                 position=[0,0],
                 color_depth=16,
                 vsync=True
                 ) -> None:
        
        self.vsync = vsync
        self.window_mode = window_mode
        self.centered = centered
        self.mouse_visible = mouse_visible
        self.color_depth = color_depth
        self.icon_path = icon_path
        self.name = window_name
        self.position = position
        self.size = window_size
        self.aspect_mode = aspect_mode
        self.surface = pygame.Surface((0,0))

        self.create()

    def create(self):
        if self.centered:
            os.environ['SDL_VIDEO_CENTERED'] = '1'
        else:
            os.environ['SDL_VIDEO_CENTERED'] = '0'

        if type(self.window_mode) != WindowMode:
            self.window_mode = WindowMode(0)

        if type(self.aspect_mode) != AspectRatioMode:
            self.aspect_mode = AspectRatioMode(-1)

        if self.size == None:
            self.size = [int(pygame.display.Info().current_w),int(pygame.display.Info().current_h)]

        if self.window_mode.type == 0: # Windowed
            self.display = pygame.display.set_mode(self.size,pygame.RESIZABLE,vsync=self.vsync,depth=self.color_depth)
            self.surface = pygame.Surface((self.size))
            self.check_window_position()
        elif self.window_mode.type == 1: # Fullscreen
            self.display = pygame.display.set_mode(self.size,pygame.FULLSCREEN,vsync=self.vsync,depth=self.color_depth)
            self.surface = pygame.Surface((self.size))
        elif self.window_mode.type == 2: # Windowed Fullscreen
            self.size = [int(pygame.display.Info().current_w),int(pygame.display.Info().current_h)]
            self.display = pygame.display.set_mode(self.size,pygame.NOFRAME,vsync=self.vsync,depth=self.color_depth)
            self.surface = pygame.Surface((self.size))
        elif self.window_mode.type == 3: # Frameless
            self.display = pygame.display.set_mode(self.size,pygame.NOFRAME,vsync=self.vsync,depth=self.color_depth)
            self.surface = pygame.Surface((self.size))
        elif self.window_mode.type == 4: # Fixed
            self.display = pygame.display.set_mode(self.size,vsync=self.vsync,depth=self.color_depth)
            self.surface = pygame.Surface((self.size))
            self.check_window_position()
        else: # No Window
            self.display = pygame.display.set_mode([0,0],pygame.HIDDEN)

        # Change window attributes
        pygame.display.set_caption(self.name)
        if self.icon_path == "":
            pygame.display.set_icon(pygame.Surface((0,0)).convert_alpha())
        else:
            pygame.display.set_icon(pygame.image.load(self.icon_path).convert_alpha())
        pygame.mouse.set_visible(self.mouse_visible)

    def update(self):
        if self.aspect_mode.type == 0: # keep aspect
            width,height = self.display.get_size()
            if (width/self.size[0] > height/self.size[1]):
                self.display.blit(pygame.transform.scale_by(self.surface,height/self.size[1]),(width/2-self.size[0]*height/self.size[1]/2,0))
            else:
                self.display.blit(pygame.transform.scale_by(self.surface,width/self.size[0]),(0,height/2-self.size[1]*width/self.size[0]/2))
        elif self.aspect_mode.type == 1: # scale content to display size
            self.display.blit(pygame.transform.scale(self.surface,self.display.get_size()),(0,0))
        else: # no scaling of content
            self.display.blit(self.surface,(0,0))
        pygame.display.update()

    def fill(self,color:list[int,int,int]):
        self.surface.fill(color)

    def render(self,sprite:pygame.Surface,pos:list[int,int],flags=0,area:pygame.Rect=None):
        self.surface.blit(sprite,pos,special_flags=flags,area=area)

    def render_rect(self,color,rect,width=0,border_radius=-1):
        pygame.draw.rect(self.surface,color,rect,width,border_radius)

    def check_window_position(self):
        window_position = pygame.display.get_window_position()
        if window_position[1] <= 0:
            pygame.display.set_window_position([window_position[0],32])

    def close(self):
        pygame.display.quit()

    def set_aspect(self,aspect_mode=KEEP,size=None):
        self.close()
        self.aspect_mode = aspect_mode
        self.size = size
        self.create()

    def set_window_mode(self,window_mode=WINDOWED):
        self.close()
        self.window_mode = window_mode
        self.create()
    
    def set_size(self,size:list[int,int]):
        self.close()
        self.window_size = size
        self.create()

    def set_vsync(self,vsync:bool):
        self.close()
        self.vsync = vsync
        self.create()
    
    def set_color_depth(self,color_depth:int):
        self.close()
        self.color_depth = color_depth
        self.create()

    def set_name(self,name:str):
        pygame.display.set_caption(str(name))

    def set_position(self,position:list[int,int]):
        pygame.display.set_window_position(position)
        self.check_window_position()

    def toggle_vsync(self):
        self.set_vsync(not(self.vsync))

    def get_position(self):
        return pygame.display.get_window_position()