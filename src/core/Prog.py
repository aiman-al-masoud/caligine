
from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict, List
from core.Ast import Ast
from core.Bool import Bool

if TYPE_CHECKING:
    from core.World import World

@dataclass
class Prog(Ast):
    statements:List[Ast]

    def execute(self, world: 'World') -> 'Ast':
        
        res:Ast = Bool(False)

        for statement in self.statements:
            res = statement.execute(world)
        
        return res

    def subst(self, dictionary: 'Ast|Dict[Ast, Ast]') -> 'Ast':
        
        return Prog([s.subst(dictionary) for s in self.statements])
