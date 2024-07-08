
from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict, List
from core.Ast import Ast

if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var

@dataclass
class Prog(Ast):
    statements:List[Ast]

    def execute(self, world: 'World') -> 'Ast':

        from core.Bool import Bool

        res:Ast = Bool(False)

        for statement in self.statements:
            res = statement.execute(world)
        
        return res
