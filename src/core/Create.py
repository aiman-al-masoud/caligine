from dataclasses import dataclass
from typing import TYPE_CHECKING
from core.Ast import Ast
from core.Object import Object

if TYPE_CHECKING:
    from core.World import World


@dataclass
class Create(Ast):

    creandum: Ast

    def execute(self, world: 'World') -> 'Ast':
        
        assert isinstance(self.creandum, Object)
        self.creandum.init(world)
        world.add_obj(self.creandum)
        return self.creandum
