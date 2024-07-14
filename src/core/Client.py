
from dataclasses import dataclass
from typing import TYPE_CHECKING
from core.Keyboard import Keyboard
from core.Object import Object
from core.Sprite import Sprite
from core.Str import Str

if TYPE_CHECKING:
    from core.World import World
    from core.Ast import Ast

@dataclass(kw_only=True)
class Client(Object):

    def init(self, world:'World')->'Ast':

        self.set('keyboard', Keyboard(name='keyboard', props={}).execute(world))
        self.set('type', Str(value='client'))
        
        if not self.has('avatar'):
            from core.Panic import Panic
            raise Panic(self, 'client must have an "avatar"')
        
        avatar = self.get('avatar').execute(world)

        if not isinstance(avatar, Sprite):
            from core.Panic import Panic
            raise Panic(self, 'the "avatar" of a client must be a sprite')
        
        return self

    def center_coords(self, world:'World'):

        avatar = self.get('avatar').execute(world)
        center_x = int(avatar.get('pos_x'))
        center_y = int(avatar.get('pos_y'))
        return center_x, center_y
    
    def get_sprite_data_from_own_perspective(self, world:'World', include_image:bool=False):

        center_x, center_y = self.center_coords(world)
        canvas_width = world.get_canvas_width()
        canvas_height = world.get_canvas_height()

        offset_x = center_x - canvas_width//2
        offset_y = center_y - canvas_height//2

        sprites = world.get_sprites()

        sprites_data = [s.to_json(
            include_image=include_image,
            offset_x = offset_x,
            offset_y = offset_y,
            ) for s in sprites]
        
        return sprites_data
    
    def see_world(self, world:'World', include_image:bool=False):

        sprites_data = self.get_sprite_data_from_own_perspective(world, include_image)

        return {
            'sprites': sprites_data, 
            'client_id': self.name,  
            'canvas_width': world.get_canvas_width(), 
            'canvas_height': world.get_canvas_height(), 
            'canvas_bg_color': world.get_canvas_bg_color(),
        }

    def __str__(self):
        return f'client{{name={self.name}}}' 


