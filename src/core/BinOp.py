from dataclasses import dataclass
from core.Ast import Ast
from typing import TYPE_CHECKING, List

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
        if left.is_shorcircuit_binop(self.op): return left
        right = self.right.execute(world)
        res = left.perform_op(self.op, right)            
        return res

    def get_vars(self) -> List['Var']:
        return self.left.get_vars()+self.right.get_vars()

    def subst(self, dictionary: 'Ast') -> 'Ast':
        return BinOp(self.op, self.left.subst(dictionary), self.right.subst(dictionary))

