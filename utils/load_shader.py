import os

def load_shader(path:str="",direct_path=None):
    if direct_path == None:
        path = os.path.join("data","shaders",path)
    else:
        path = direct_path

    with open(path,"r", encoding="utf-8") as f:
        data = f.read()
        f.close()
        return data