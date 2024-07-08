from dataclasses import dataclass
from core.Ast import Ast
from typing import TYPE_CHECKING, Dict, List


if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var


@dataclass
class BinOp(Ast):
    op:str
    left:'Ast'
    right:'Ast'

    def execute(self, world: 'World') -> 'Ast':

        left = self.left.execute(world)
        right = self.right.execute(world)
        return left.perform_op(self.op, right)

    def get_vars(self) -> List['Var']:
        return self.left.get_vars()+self.right.get_vars()

    def subst(self, d: Dict['Ast', 'Ast']) -> 'Ast':
        return BinOp(self.op, self.left.subst(d), self.right.subst(d))
