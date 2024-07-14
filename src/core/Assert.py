from dataclasses import dataclass
from typing import TYPE_CHECKING
from core.Ast import Ast
from core.Bool import Bool
from core.Panic import Panic

if TYPE_CHECKING:
    from core.World import World

@dataclass
class Assert(Ast):

    assertion:Ast

    def execute(self, world: 'World') -> 'Ast':
        
        if not self.assertion.execute(world):
            raise Panic(self, 'assertion failed')#.execute(world)
        
        return Bool(True)

