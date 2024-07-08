
from dataclasses import dataclass
from typing import TYPE_CHECKING
from core.Ast import Ast

if TYPE_CHECKING:
    from core.World import World

@dataclass
class Assert(Ast):

    assertion:Ast
    line_num:int

    def execute(self, world: 'World') -> 'Ast':
        
        from core.Bool import Bool
        if not self.assertion.execute(world):
            world.error(f'Assertion failed at line={self.line_num}')
            
        return Bool(True)

