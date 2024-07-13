from dataclasses import dataclass
from core.Ast import Ast
from core.Bool import Bool
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var

@dataclass
class Not(Ast):
    negated:Ast

    def execute(self, world: 'World') -> 'Ast':

        ast = self.negated.execute(world)
        return Bool(not bool(ast))
 
    def get_vars(self) -> List['Var']:
        return self.negated.get_vars()

    def subst(self, dictionary: 'Ast') -> 'Ast':
        return Not(self.negated.subst(dictionary))
