
from core.Ast import Ast
from dataclasses import dataclass


from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var

from typing import TYPE_CHECKING, Dict, List


@dataclass
class Del(Ast):
    delendum:Ast

    def execute(self, world: 'World') -> 'Ast':

        from core.Object import Object
        from core.Bool import Bool

        delendum = self.delendum.execute(world)
        assert isinstance(delendum, Object)

        world.rm_obj(delendum.name)
        return Bool(True)

    def get_vars(self) -> List['Var']:
        return self.delendum.get_vars()

    def subst(self, d: Dict['Ast', 'Ast']) -> 'Ast':
        return Del(self.delendum.subst(d))
