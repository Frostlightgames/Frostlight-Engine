from __init__ import *

class Window:
    """
    The window to render sprites on.

    Attributes:
        size (list[int]): Window dimensions [width, height].
        ctx (moderngl.Context): The ModernGL context.
        clock (pygame.time.Clock): Clock for framerate control.
        render_queue (list): A queue of sprites to render.

    Example:
        >>> self.window = Window(1280, 720, "My Game")
        >>> self.window.clear()
        >>> self.window.render(player, [100, 150], [2.0, 2.0])
        >>> self.window.update()
    """
    
    def __init__(self, width=1920, height=1080, title="New game"):
        """
        Initialize the rendering window.

        Args:
            width (int): Width of the window in pixels. Defaults to 1920.
            height (int): Height of the window in pixels. Defaults to 1080.
            title (str): Title of the window. Defaults to "New game".
        """
        pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

        self.ctx = moderngl.create_context(require=430)
        self.ctx.viewport = (0, 0, width, height)
        self.ctx.enable(moderngl.BLEND)
        self.ctx.blend_func = (moderngl.SRC_ALPHA, moderngl.ONE_MINUS_SRC_ALPHA)

        self.size = [width, height]
        self.render_queue = []

    def clear(self):
        """
        Clear the screen and reset the render queue.

        This should be called before rendering a new frame.

        Example:
            >>> self.window.clear()
        """
        self.ctx.clear(0.0, 0.0, 0.0)
        self.render_queue.clear()

    def render(self, sprite, position=[0, 0], scale=None):
        """
        Queue a sprite to be rendered.

        Args:
            sprite: (Sprite): The sprite object that should be drawn.
            position (list[int]): Screen position [x, y] to render the sprite.
            scale (list[float] or None): Optional scale for the sprite.

        Example:
            >>> self.window.render(player, [100, 200], [1.5, 1.5])
        """
        self.render_queue.append((sprite, position, scale))

    def set_size(self, width, height):
        """
        Set a new window size.

        Args:
            width (int): New width.
            height (int): New height.

        Example:
            >>> win.set_size(800, 600)
        """
        self.size = [width, height]

    def update(self):
        """
        Process the render queue and draw sprites to the screen.

        This should be called once per frame after.

        Example:
            >>> self.window.update()
        """
        sprite_batches = {}

        # Group render instances by sprite to reduce state changes
        for sprite, pos, scale in self.render_queue:
            if sprite not in sprite_batches:
                sprite_batches[sprite] = []
            sprite_batches[sprite].append((pos, scale))

        # Render all sprite instances
        for sprite, instances in sprite_batches.items():
            sprite.texture.use()

            for pos, scale in instances:
                sprite.set_uniforms(pos, self.size, scale)
                sprite.vao.render(moderngl.TRIANGLE_STRIP)

        pygame.display.flip()