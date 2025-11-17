from init import *
from utils.load_shader import load_shader
class Window:
    def __init__(self, window_size:list = [1920,1080], canvas_size:list=[1920,1080], mode=pygame.RESIZABLE, title="New game"):
        pygame.display.set_mode(window_size, pygame.DOUBLEBUF | pygame.OPENGL | mode)
        pygame.display.set_caption(title)

        self.window_size = window_size
        self.canvas_size = canvas_size

        self._render_queue = []

        self._ctx = moderngl.create_context(require=330)
        self._ctx.enable(moderngl.BLEND)
        self._ctx.blend_func = (moderngl.SRC_ALPHA, moderngl.ONE_MINUS_SRC_ALPHA)
        
        self._texture = self._ctx.texture(self.canvas_size, 4)
        self._texture.filter = (moderngl.NEAREST, moderngl.NEAREST)
        self._canvas_tex = self._ctx.texture(self.canvas_size, 4)
        self._canvas_tex.filter = (moderngl.NEAREST, moderngl.NEAREST)
        self._canvas_fbo = self._ctx.framebuffer([self._canvas_tex])

        self.program = self._ctx.program(load_shader("window.vert"),load_shader("window.frag"))

        self._vbo = self._ctx.buffer(numpy.array([-1.0, -1.0, 0.0, 0.0, 1.0, -1.0, 1.0, 0.0, -1.0,  1.0, 0.0, 1.0, 1.0,  1.0, 1.0, 1.0,], dtype="f4"))
        self._vao = self._ctx.vertex_array(self.program, [(self._vbo, "2f 2f", "in_vert", "in_uv")])

    def clear(self):
        self._ctx.clear(0.0, 0.0, 0.0)
        self._render_queue.clear()

    def render(self, sprite, position=[0, 0], centered=False):
        self._render_queue.append((sprite, position, centered))

    def fill(self, red=0, green=0, blue=0):
        self._canvas_fbo.use()
        self._ctx.clear(red / 255.0, green / 255.0, blue / 255.0, 1.0)

    def resize(self, new_size):
        self.window_size = new_size
        self._ctx.viewport = (0, 0, *self.window_size)

    def update(self):
        self._canvas_fbo.use()
        for sprite, pos, centered in self._render_queue:
            sprite._render(pos, self.canvas_size, centered)

        self._ctx.screen.use()
        self._ctx.clear(0.0, 0.0, 0.0, 1.0)

        self._canvas_tex.use()
        self._vao.render(moderngl.TRIANGLE_STRIP)

        pygame.display.flip()
        self.clear()