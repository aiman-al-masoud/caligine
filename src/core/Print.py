
from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict
from core.Ast import Ast
from core.Bool import Bool

if TYPE_CHECKING:
    from core.World import World

@dataclass
class Print(Ast):
    prindandum:Ast

    def execute(self, world: 'World') -> 'Ast':
    
        world.print(str(self.prindandum.execute(world)))
        return Bool(True)
    
    def subst(self, dictionary: 'Ast|Dict[Ast, Ast]') -> 'Ast':
        return Print(self.prindandum.subst(dictionary))
