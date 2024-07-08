
from dataclasses import dataclass
from typing import TYPE_CHECKING
from core.Ast import Ast

if TYPE_CHECKING:
    from core.World import World

@dataclass
class Print(Ast):
    prindandum:Ast

    def execute(self, world: 'World') -> 'Ast':
        
        from core.Bool import Bool
        world.print(str(self.prindandum.execute(world)))
        return Bool(True)
