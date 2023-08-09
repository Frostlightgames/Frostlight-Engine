import pygame

class Text:
    def render(engine,text:str,pos:list,font=1):
        if font == 1:
            surf = pygame.Surface((len(text)*engine.font.width+len(text)*engine.font.width/4,engine.font.height)).convert_alpha()
            for i,letter in enumerate(text):
                if letter != " ":
                    surf.blit(engine.font.get(letter),(i*engine.font.width+i*engine.font.width/4,0))
            surf.set_colorkey((0,0,0))
            engine.win.blit(surf,pos)
        else:
            surf = pygame.Surface((len(text)*engine.font2.width+len(text)*engine.font2.width/4,engine.font2.height)).convert_alpha()
            for i,letter in enumerate(text):
                if letter != " ":
                    surf.blit(engine.font2.get(letter),(i*engine.font2.width+i*engine.font2.width/4,0))
            surf.set_colorkey((0,0,0))
            engine.win.blit(surf,pos)

    def render_to(engine,text:str,pos:list,surf):
        textsurf = pygame.Surface((len(text)*engine.font.width+len(text)*engine.font.width/4,engine.font.height)).convert_alpha()
        for i,letter in enumerate(text):
            if letter != " ":
                textsurf.blit(engine.font.get(letter),(i*engine.font.width+i*engine.font.width/4,0))
        surf.set_colorkey((0,0,0))
        surf.blit(textsurf,pos)
    
    def get_size(engine,text:str,fonttype=1) -> pygame.Rect:
        if fonttype == 1:
            return pygame.Rect(0,0,len(text)*engine.font.width+len(text)*engine.font.width/4,engine.font.height)
        else:
            return pygame.Rect(0,0,len(text)*engine.font2.width+len(text)*engine.font2.width/4,engine.font2.height)