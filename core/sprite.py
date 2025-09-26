from init import *
import init as init

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

    def __init__(self, image_path, size:list=None):
        """
        Initializes the Sprite by loading the texture, compiling shaders,
        and setting up buffers for rendering.

        Args:
            image_path (str): Path to the image file used as the sprite's texture.
        """

        self.__ctx = init.WINDOW_CONTEXT
        self.__size = [1.0,1.0]
        self._texture = self.__load_texture(image_path)
        self.__program = self.__create_program()
        self.__vbo = self.__create_quad()
        self._vao = self.__ctx.vertex_array(self.__program,[(self.__vbo, '2f 2f', 'in_vert', 'in_tex')])
        self.__alpha = 1.0
        self.__rotation = 0
        self.__pivot_point = [0.0,0.0]

        if size != None:
            self.set_size(size)

    def set_alpha(self, alpha:float=1.0):
        if alpha > 1.0 or alpha < 0.0:
            raise ValueError("Alpha value must be between 0.0 and 1.0")
        
        self.__alpha = alpha

    def get_alpha(self):
        return self.__alpha

    def set_rotation(self, rotation:float=0.0):
        self.__rotation = rotation

    def get_rotation(self):
        return self.__rotation
    
    def set_size(self, size:list=[1.0,1.0]):
        if size[0] < 0 or size[1] < 0:
            raise ValueError("Any size parameter must be larger than 0")
        
        self.__size = size

    def get_size(self):
        return self.__size
    
    def scale_by(self, factor:float=1.0):
        if factor < 0.0:
            raise ValueError("Sizing factor must be larger than 0")
        
        self.set_size([self.__size[0]*factor,self.__size[1]*factor])

    def set_pivot_point(self, pivot_point:list=[0.0,0.0]):
        self.__pivot_point = pivot_point

    def get_pivot_point(self):
        return self.__pivot_point

    def __create_program(self):
        """
        Compiles and links the vertex and fragment shaders into a ModernGL program.

        Returns:
            moderngl.Program: The compiled shader program.
        """
         
        return self.__ctx.program(
            vertex_shader="""
                #version 330
                uniform vec2 offset;
                uniform vec2 scale_pixels;
                uniform vec2 screen_size;
                uniform float rotation;
                uniform float alpha;
                uniform vec2 pivot;

                in vec2 in_vert;
                in vec2 in_tex;
                out vec2 v_tex;

                void main() {
                    float c = cos(rotation);
                    float s = sin(rotation);

                    vec2 local = in_vert - pivot;
                    vec2 scaled = local * scale_pixels;
                    vec2 rotated = vec2(
                        scaled.x * c - scaled.y * s,
                        scaled.x * s + scaled.y * c
                    );

                    vec2 transformed = rotated + pivot * scale_pixels;
                    vec2 ndc = vec2(
                        transformed.x * 2.0 / screen_size.x,
                        transformed.y * 2.0 / screen_size.y
                    );

                    gl_Position = vec4(offset + ndc, 0.0, 1.0);
                    v_tex = in_tex;
                }
            """,
            fragment_shader="""
                #version 330
                uniform sampler2D Texture;
                uniform float alpha;
                in vec2 v_tex;
                out vec4 fragColor;

                void main() {
                    vec4 texColor = texture(Texture, v_tex);
                    fragColor = vec4(texColor.rgb, texColor.a * alpha);
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
        return self.__ctx.buffer(vertices.tobytes())

    def __load_texture(self, path):
        """
        Loads an image and creates an OpenGL texture.

        Args:
            path (str): File path to the image.

        Returns:
            moderngl.Texture: The OpenGL texture object.
        """

        img = Image.open(path).convert('RGBA')
        self.__width, self.__height = img.size
        self.__size = [self.__width,self.__height]
        texture = self.__ctx.texture((self.__width, self.__height), 4, img.tobytes())

        texture.filter = (moderngl.NEAREST, moderngl.NEAREST)

        texture.use()
        return texture
    
    def _set_uniforms(self, pos, screen_size, centered):
        if centered:
            normal_x = (pos[0] / screen_size[0]) * 2.0 - 1.0
            normal_y = 1.0 - (pos[1] / screen_size[1]) * 2.0
        else:
            normal_x = ((pos[0] + self.__size[0] / 2.0) / screen_size[0]) * 2.0 - 1.0
            normal_y = 1.0 - ((pos[1] + self.__size[1] / 2.0) / screen_size[1]) * 2.0

        size_x = float(self.__size[0])
        size_y = float(self.__size[1])

        self.__program['offset'].value = (normal_x, normal_y)
        self.__program['scale_pixels'].value = (size_x, size_y)
        self.__program['screen_size'].value = (float(screen_size[0]), float(screen_size[1]))
        self.__program['rotation'].value = math.radians(-self.__rotation)
        self.__program['alpha'].value = self.__alpha
        self.__program['pivot'].value = self.__pivot_point
        self._texture.use()


