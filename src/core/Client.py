
from dataclasses import dataclass
from typing import TYPE_CHECKING
from core.Keyboard import Keyboard
from core.Object import Object
from core.Sprite import Sprite


if TYPE_CHECKING:
    from core.World import World


@dataclass
class Client(Object):

    def __post_init__(self):
        self.set('keyboard', Keyboard('keyboard', {}))

    def center_coords(self, world:'World'):

        avatar = self.get('avatar').execute(world)
        assert isinstance(avatar, Sprite)

        center_x = int(avatar.get('pos_x'))
        center_y = int(avatar.get('pos_y'))
        return center_x, center_y
    # def look_at_world(self, world:'World', canvas:'Canvas'):
        
    #     avatar = self.get('avatar').execute(world)
    #     assert isinstance(avatar, Sprite)

    #     center_x = int(avatar.get('pos_x'))
    #     center_y = int(avatar.get('pos_y'))

    #     world.draw(canvas, center_x, center_y)
