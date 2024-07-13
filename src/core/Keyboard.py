from dataclasses import dataclass
from typing import TYPE_CHECKING
from core.Object import Object
from core.Str import Str

if TYPE_CHECKING:
    from core.World import World


@dataclass
class Keyboard(Object):

    def init(self, world: 'World'):
        self.set('type', Str('keyboard'))
