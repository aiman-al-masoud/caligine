from dataclasses import dataclass, field
from core.Ast import Ast
from typing import TYPE_CHECKING, List, Optional

from core.MetaInfo import MetaInfo

if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var


@dataclass(kw_only=True)
class BinOp(Ast):
    op: str
    left: 'Ast'
    right: 'Ast'
    meta_info: Optional[MetaInfo] = field(default=None, compare=False)

    def execute(self, world: 'World') -> 'Ast':

        left = self.left.execute(world)
        if left.is_shorcircuit_binop(self.op):
            return left
        right = self.right.execute(world)
        res = left.perform_op(self.op, right)
        return res

    def get_vars(self) -> List['Var']:
        return self.left.get_vars()+self.right.get_vars()

    def subst(self, dictionary: 'Ast') -> 'Ast':
        return BinOp(op=self.op, left=self.left.subst(dictionary), right=self.right.subst(dictionary))
