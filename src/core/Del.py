
from core.Ast import Ast
from dataclasses import dataclass
from core.Object import Object
from core.Bool import Bool
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var


@dataclass
class Del(Ast):
    delendum:Ast

    def execute(self, world: 'World') -> 'Ast':

        # TODO: Remove assertion. Assign rather than create-with-name
        delendum = self.delendum.execute(world)
        assert isinstance(delendum, Object)
        world.rm_obj(delendum.name)
        return Bool(True)

    def get_vars(self) -> List['Var']:
        return self.delendum.get_vars()

    def subst(self, dictionary: 'Ast') -> 'Ast':
        return Del(self.delendum.subst(dictionary))
