from dataclasses import dataclass
from typing import TYPE_CHECKING
from core.Object import Object
from core.Str import Str

if TYPE_CHECKING:
    from core.World import World
    from core.Ast import Ast


@dataclass(kw_only=True)
class Keyboard(Object):

    def init(self, world: 'World')->'Ast':
        
        self.set('type', Str(value='keyboard'))
        return self
