from init import *

class Builder:
    def __init__(self):
        os.makedirs(os.path.join("screenshots"),exist_ok=True)
        os.makedirs(os.path.join("data","classes"),exist_ok=True)
        os.makedirs(os.path.join("data","logs"),exist_ok=True)
        os.makedirs(os.path.join("data","saves"),exist_ok=True)
        os.makedirs(os.path.join("data","shaders"),exist_ok=True)
        os.makedirs(os.path.join("data","sprites"),exist_ok=True)
