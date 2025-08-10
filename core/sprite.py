from __init__ import *
import __init__ as init

class Sprite:
    """
    A 2D textured sprite.

    This sprite uses a textured quad rendered via OpenGL shaders,
    allowing positioning, scaling, and rotation in screen space.

    Attributes:
        ctx: The ModernGL context (retrieved from global WINDOW_CONTEXT).
        texture: The loaded OpenGL texture.
        program: The ModernGL shader program used for rendering.
        vbo: Vertex Buffer Object containing quad vertex data.
        vao: Vertex Array Object used to bind shaders and buffers for drawing.
        width: Width of the loaded texture in pixels.
        height: Height of the loaded texture in pixels.
    """

    def __init__(self, image_path):
        """
        Initializes the Sprite by loading the texture, compiling shaders,
        and setting up buffers for rendering.

        Args:
            image_path (str): Path to the image file used as the sprite's texture.
        """

        self.ctx = init.WINDOW_CONTEXT
        self.texture = self.__load_texture(image_path)
        self.program = self.__create_program()
        self.vbo = self.__create_quad()
        self.vao = self.ctx.vertex_array(self.program,[(self.vbo, '2f 2f', 'in_vert', 'in_tex')])

    def __create_program(self):
        """
        Compiles and links the vertex and fragment shaders into a ModernGL program.

        Returns:
            moderngl.Program: The compiled shader program.
        """
         
        return self.ctx.program(
            vertex_shader="""
                #version 330
                uniform vec2 offset;
                uniform vec2 scale;
                uniform float rotation;

                in vec2 in_vert;
                in vec2 in_tex;
                out vec2 v_tex;

                void main() {
                    float c = cos(rotation);
                    float s = sin(rotation);
                    vec2 rotated = vec2(
                        in_vert.x * c - in_vert.y * s,
                        in_vert.x * s + in_vert.y * c
                    );
                    gl_Position = vec4(offset + rotated * scale, 0.0, 1.0);
                    v_tex = in_tex;
                }
            """,
            fragment_shader="""
                #version 330
                uniform sampler2D Texture;
                in vec2 v_tex;
                out vec4 fragColor;

                void main() {
                    fragColor = texture(Texture, v_tex);
                }
            """
        )

    def __create_quad(self):
        """
        Creates a quad with position and texture coordinates.

        The quad is centered at (0,0) and spans from -0.5 to 0.5.

        Returns:
            moderngl.Buffer: Vertex buffer for the quad.
        """

        vertices = numpy.array([
            -0.5, -0.5, 0.0, 1.0,
             0.5, -0.5, 1.0, 1.0,
            -0.5,  0.5, 0.0, 0.0,
             0.5,  0.5, 1.0, 0.0,
        ], dtype='f4')
        return self.ctx.buffer(vertices.tobytes())

    def __load_texture(self, path):
        """
        Loads an image and creates an OpenGL texture.

        Args:
            path (str): File path to the image.

        Returns:
            moderngl.Texture: The OpenGL texture object.
        """

        img = Image.open(path).convert('RGBA')
        self.width, self.height = img.size
        texture = self.ctx.texture((self.width, self.height), 4, img.tobytes())

        texture.filter = (moderngl.NEAREST, moderngl.NEAREST)

        texture.use()
        return texture
    
    def _set_uniforms(self, pos, screen_size, scale=None, rotation=0, centered=True):
        """
        Sets shader uniforms for rendering the sprite on screen.

        Args:
            pos (list): (x, y) position in pixels on the screen.
            screen_size (list): (width, height) of the window or framebuffer.
            scale (list or None): Optional (width, height) scale in pixels. Defaults to texture size.
            rotation (float): Rotation in radians.
        """

        # Convert screen position to normalized device coordinates (NDC)

        if not centered:
            pos[0] = pos[0] + scale[0]/4
            pos[1] = pos[1] + scale[1]/4
            
        normal_x = (pos[0] / screen_size[0]) * 2.0 - 1.0
        normal_y = 1.0 - (pos[1] / screen_size[1]) * 2.0

        # Determine scale in NDC
        if scale is None:
            scale_x = self.width
            scale_y = self.height
        else:
            scale_x = scale[0]
            scale_y = scale[1]

        normal_scale_x = scale_x / screen_size[0]
        normal_scale_y = scale_y / screen_size[1]

        # Set shader uniforms
        self.program['offset'].value = (normal_x, normal_y)
        self.program['scale'].value = (normal_scale_x, normal_scale_y)
        self.program['rotation'].value = float(rotation)
        self.texture.use()
