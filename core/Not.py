from dataclasses import dataclass
from core.Ast import Ast

from typing import TYPE_CHECKING, Dict, List

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var


@dataclass
class Not(Ast):
    negated:Ast

    def execute(self, world: 'World') -> 'Ast':

        from core.Bool import Bool

        ast = self.negated.execute(world)
        return Bool(not bool(ast))
 
    def get_vars(self) -> List['Var']:
        return self.negated.get_vars()

    def subst(self, d: Dict['Ast', 'Ast']) -> 'Ast':
        return Not(self.negated.subst(d))