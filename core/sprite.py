from init import *
from utils.load_shader import load_shader

class Sprite:
    def __init__(self, image_path=None, size:list=None, texture_filter=moderngl.NEAREST, direct_image_path=None):
        self.alpha = 1.0
        self.flipped = False
        self.pivot_point = [0,0]
        self.rotation = 0
        self.size = [1,1]

        if size != None:
            self.size = size

        if direct_image_path == None:
            if image_path != None:
                image_path = os.path.join("data","sprites",image_path)
        else:
            image_path = direct_image_path

        self._ctx:moderngl.Context = GLOBAL_ENVIRONMENT.MODERNGL_CONTEXT
        self._texture = self._load_texture(image_path,texture_filter,size)
        self._program = self._ctx.program(load_shader("default.vert"),load_shader("default.frag"))
        self._vbo = self._ctx.buffer(numpy.array([-0.5, 0.5, 0.0, 0.0, 0.5, 0.5, 1.0, 0.0, -0.5, -0.5, 0.0, 1.0, 0.5, -0.5, 1.0, 1.0,],"f4"))
        self._vao = self._ctx.vertex_array(self._program,[(self._vbo,"2f 2f", "vert", "tex")])
        self._custom_program: moderngl.Program = None

        self.custom_uniforms = {}

    @property
    def alpha(self):
        return self._alpha
    
    @alpha.setter
    def alpha(self, value:float=1.0):
        if type(value) not in [int,float] or value > 1.0 or value < 0.0:
            raise ValueError("Alpha value must be between 0.0 and 1.0")
        
        self._alpha = value

    @property
    def flipped(self):
        return self._flipped
    
    @flipped.setter
    def flipped(self, value:int|bool=False):
        if type(value) not in [bool,int] or value not in [0,1]:
            raise ValueError("Flipped must be a boolean, 0 or 1")
        
        self._flipped = value

    @property
    def pivot_point(self):
        return self._pivot_point
    
    @pivot_point.setter
    def pivot_point(self, value:list[float]=[0.0,0.0]):
        if type(value) != list or type(value[0]) not in [int,float] or type(value[1]) not in [int,float] or len(value) != 2:
            raise ValueError("Pivot Point must be a list with 2 floats")
        
        self._pivot_point = value

    @property
    def rotation(self):
        return self._rotation
    
    @rotation.setter
    def rotation(self, value:int|int=0):
        if type(value) not in [int,float]:
            raise ValueError("Rotation must be a integer or float")
        
        self._rotation = value

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value:list[int]=[1,1]):
        if type(value) != list or type(value[0]) != int or type(value[1]) != int or len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise ValueError("Size must be a list with 2 positive integer")
        
        self._size = value

    def scale_by(self,factor:float=2.0):
        if factor < 0.0:
            raise ValueError("Sizing factor must be larger than 0")
        
        self.size = [int(self.size[0]*factor),int(self.size[1]*factor)]

    def set_custom_shader(self, fragment_shader_path:str):
        new_program = self._ctx.program(load_shader("default.vert"), load_shader(fragment_shader_path))
        self._vao.release()
        self._program.release()
        self._program = new_program
        self._vao = self._ctx.vertex_array(self._program, [(self._vbo, "2f 2f", "vert", "tex")])

    def _load_texture(self,path,texture_filter,preferred_size):
        texture = None
        self.size = [1,1]
        if path != None:
            img = Image.open(path).convert('RGBA')
            self.size = [img.size[0],img.size[1]]
            texture = self._ctx.texture(self.size, 4, img.tobytes())
        else:
            texture = self._ctx.texture(self.size, 4)
        texture.filter = (texture_filter, moderngl.NEAREST)
        texture.repeat_x = False
        texture.repeat_y = False

        if preferred_size != None:
            self.size = preferred_size

        return texture
    
    def set_custom_uniforms(self, uniform, value):
        self.custom_uniforms[uniform] = value
    
    def _render(self, pos, canvas_size, centered):
        if centered:
            normal_x = (pos[0] / canvas_size[0]) * 2.0 - 1.0
            normal_y = 1.0 - (pos[1] / canvas_size[1]) * 2.0
        else:
            normal_x = ((pos[0] + self.size[0] / 2.0) / canvas_size[0]) * 2.0 - 1.0
            normal_y = 1.0 - ((pos[1] + self.size[1] / 2.0) / canvas_size[1]) * 2.0

        size_x = float(self.size[0])
        size_y = float(self.size[1])

        if "offset" in self._program:
            self._program["offset"].value = (normal_x, normal_y)
        if "scale_pixels" in self._program:
            self._program["scale_pixels"].value = (size_x, size_y)
        if "screen_size" in self._program:
            self._program["screen_size"].value = (float(canvas_size[0]), float(canvas_size[1]))
        if "rotation" in self._program:
            self._program["rotation"].value = math.radians(-self.rotation)
        if "alpha" in self._program:
            self._program["alpha"].value = self.alpha
        if "flipped" in self._program:
            self._program["flipped"].value = self.flipped

        for uniform in self.custom_uniforms:
            self._program[uniform].value = self.custom_uniforms[uniform]

        self.custom_uniforms.clear()
        
        self._texture.use()
        self._vao.render(moderngl.TRIANGLE_STRIP)