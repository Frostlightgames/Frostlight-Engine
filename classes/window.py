import os
import pygame

class Window:
    def __init__(self,engine,set_window_size=None,fullscreen=False,resizable=True,windowless=False,window_centered=True,vsync=False,window_name="Frostlight Engine",mouse_visible=True,color_depth=24) -> None:
        
        """
        Initialise the engines window system.

        The window system manages all window events and rendering.

        Args:
        
        - engine (Engine): The engine to access specific variables.
        - set_window_size (list)=None: Size of window.
        - fullscreen (bool)=False: Sets windows fullscreen mode.
        - resizable (bool)=True: Sets windows resizability.
        - windowless (bool)=False: Removes window interaction menu at the top.
        - window_centered (bool)=True: Sets window centered state.
        - vsync (bool)=False: Sets vsync state.
        - window_name (str)="Frostlight Engine": Default name to display.
        - mouse_visible (bool)=True: mouses visibility state.
        - color_depth (int)=24: Window color depth.

        !!!This is only used internally by the engine and should not be called in a game!!!
        """

        # Engine Variable
        self.engine = engine

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

    def _create(self):

        """
        Creates main window instance.

        Args:
        
        - no args are required.

        !!!This is only used internally by the engine and should not be called in a game!!!
        """

        if not self.windowless:
            pygame.display.init()
            
            # Center window
            if self.window_centered:
                os.environ['SDL_VIDEO_CENTERED'] = '1'
            else:
                os.environ['SDL_VIDEO_CENTERED'] = '0'

            # Create window
            display_size = [int(pygame.display.Info().current_w),int(pygame.display.Info().current_h)]
            if self.fullscreen: 
                
                # Fullscreen window
                self.main_surface = pygame.display.set_mode(display_size,pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN,vsync=self.vsync,depth=self.color_depth)
            else:

                # Calculate fitting window size
                if self.window_size == None:
                    self.window_size = [display_size[0],display_size[1]*0.94]

                if self.resizable:
                    
                    # Resizable window
                    self.main_surface = pygame.display.set_mode(self.window_size,pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE,vsync=self.vsync,depth=self.color_depth)
                else: 
                    
                    # Fixed size window
                    self.main_surface = pygame.display.set_mode(self.window_size,pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.NOFRAME,vsync=self.vsync,depth=self.color_depth)
            
            # Change window attributes
            pygame.display.set_caption(self.window_name)
            pygame.mouse.set_visible(self.mouse_visible)

    def render(self,sprite:pygame.Surface,pos:list[int,int] | pygame.Rect):

        """
        Renders a sprite to the main window.

        Args:
        
        - sprite (pygame.Surface): The sprite to render.
        - pos (list[int,int]): The position to render the sprite to.

        Example:
        ```
        self.window.render(player_sprite,player_pos)
        ```
        """

        # Renders sprite to main window
        self.main_surface.blit(sprite,pos)

    def resize(self,new_window_size:list[int,int]):

        """
        Resizes the main window.

        Args:
        
        - new_window_size (list[int,int]): The new window size.

        Example:
        ```
        self.window.resize([600,600])
        ```
        """

        # Resize window to specified size        
        self.window_size = new_window_size

        if self.resizable:

            # Resizable window 
            self.main_surface = pygame.display.set_mode(self.window_size,pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE,vsync=self.vsync,depth=self.color_depth)
        else: 
            
            # Fixed size window
            self.main_surface = pygame.display.set_mode(self.window_size,pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.NOFRAME,vsync=self.vsync,depth=self.color_depth)

    def set_fullscreen(self,fullscreen:bool):

        """
        Changes window fullscreen state.

        Args:
        
        - fullscreen (bool): Fullscreen state.

        Example:
        ```
        self.window.set_fullscreen(True)
        ```
        """

        # Set fullscreen variable
        self.fullscreen = fullscreen
        pygame.display.quit()
        self._create()

    def toggle_fullscreen(self):

        """
        Toggles window fullscreen state.

        Args:
        
        - no args are required.

        Example:
        ```
        self.window.toggle_fullscreen()
        ```
        """

        # Set Fullscreen variable to opposite truth value
        self.set_fullscreen(not(self.fullscreen))

    def set_name(self,name:str="") -> None:

        """
        Set a window name.

        Args:
        
        - name (str)="": New window name.

        Example:
        ```
        self.window.set_name("new game")
        ```
        """

        # Renaming the displayed window title
        pygame.display.set_caption(str(name))

    def get_fps(self) -> int:

        """
        Returns games fps value.

        Args:
        
        - no args are required.

        Returns:

        - FPS value as integer.

        Example:
        ```
        self.window.set_name(self.window.get_fps())
        ```
        """

        # Returning frames per second as integer
        return int(min(self.engine.clock.get_fps(),99999999))
    
    def fill(self,color:list[int,int,int]) -> None:

        """
        Fills window with a color.

        Args:
        
        - color (list[int,int,int]): Color the window is filled with.

        Example:
        ```
        self.window.fill([3,13,36])
        ```
        """

        # Fills the screen with a solid color
        self.main_surface.fill(color)