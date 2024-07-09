
from dataclasses import dataclass
from typing import TYPE_CHECKING
from core.Object import Object
from canvas import Canvas
from core.Sprite import Sprite


if TYPE_CHECKING:
    from core.World import World


@dataclass
class Client(Object):
    
    def look_at_world(self, world:'World', canvas:'Canvas'):
        
        avatar = self.get('avatar').execute(world)
        assert isinstance(avatar, Sprite)

        center_x = int(avatar.get('pos_x'))
        center_y = int(avatar.get('pos_y'))

        WINDOW_SIZE = 400
        left_x = center_x - WINDOW_SIZE//2
        top_y = center_y - WINDOW_SIZE//2

        world.draw(canvas, left_x, top_y, WINDOW_SIZE, WINDOW_SIZE) 
