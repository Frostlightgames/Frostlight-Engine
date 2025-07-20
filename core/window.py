from __init__ import *

class Window:
    def __init__(self, width=1920, height=1080, title="New game"):
        pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.OPENGL)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

        self.ctx = moderngl.create_context(require=430)
        self.ctx.viewport = (0, 0, width, height)
        self.ctx.enable(moderngl.BLEND)
        self.ctx.blend_func = (moderngl.SRC_ALPHA,moderngl.ONE_MINUS_SRC_ALPHA)

        self.size = [width, height]
        self.render_queue = []

    def clear(self):
        self.ctx.clear(0.1, 0.0, 0.0)
        self.render_queue.clear()

    def render(self, sprite, position=[0,0], scale=None):
        self.render_queue.append((sprite, position, scale))

    def set_size(self,width,height):
        self.size = [width,height]
        
    def update(self):
        sprite_batches = {}

        for sprite, pos, scale in self.render_queue:
            if sprite not in sprite_batches:
                sprite_batches[sprite] = []
            sprite_batches[sprite].append((pos, scale))

        for sprite, instances in sprite_batches.items():
            sprite.texture.use()

            for pos, scale in instances:
                sprite.set_uniforms(pos, self.size, scale)
                sprite.vao.render(moderngl.TRIANGLE_STRIP)

        pygame.display.flip()