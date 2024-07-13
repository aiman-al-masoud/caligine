from dataclasses import dataclass
from typing import TYPE_CHECKING, List
from core.Ast import Ast
from core.Bool import Bool
from core.Panic import Panic

if TYPE_CHECKING:
    from core.World import World

@dataclass
class Prog(Ast):
    statements:List[Ast]

    def execute(self, world: 'World') -> 'Ast':
        
        res:Ast = Bool(False)

        for statement in self.statements:

            res = statement.execute(world)

            if isinstance(res, Panic):
                res.execute(world)
                return res
        
        return res

    def subst(self, dictionary: 'Ast') -> 'Ast':
        
        return Prog([s.subst(dictionary) for s in self.statements])
