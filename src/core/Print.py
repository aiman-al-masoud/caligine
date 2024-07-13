
from dataclasses import dataclass
from typing import TYPE_CHECKING
from core.Ast import Ast
from core.Bool import Bool

if TYPE_CHECKING:
    from core.World import World

@dataclass
class Print(Ast):
    prindandum:Ast

    def execute(self, world: 'World') -> 'Ast':

        world.stdout.write(str(self.prindandum.execute(world))+'\n') 
        world.stdout.flush()
        # world.print(str(self.prindandum.execute(world)))
        return Bool(True)
    
    def subst(self, dictionary: 'Ast') -> 'Ast':
        return Print(self.prindandum.subst(dictionary))
