
from dataclasses import dataclass
from typing import TYPE_CHECKING
from core.Keyboard import Keyboard
from core.Object import Object
from core.Sprite import Sprite
from core.Str import Str

if TYPE_CHECKING:
    from core.World import World

@dataclass
class Client(Object):

    def init(self, world: 'World'):

        self.set('keyboard', Keyboard('keyboard', {}).execute(world))
        self.set('type', Str('client'))

    def center_coords(self, world:'World'):

        avatar = self.get('avatar').execute(world)
        assert isinstance(avatar, Sprite)
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

    def __str__(self):
        return f'client{{name={self.name}}}' 


