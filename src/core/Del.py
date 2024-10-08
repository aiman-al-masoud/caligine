
from core.Ast import Ast
from dataclasses import dataclass, field
from core.MetaInfo import MetaInfo
from core.Object import Object
from core.Bool import Bool
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var


@dataclass(kw_only=True)
class Del(Ast):

    delendum: Ast
    meta_info: Optional[MetaInfo] = field(default=None, compare=False)

    def execute(self, world: 'World') -> 'Ast':

        # TODO: Remove assertion. Assign rather than create-with-name
        # or delete the reference, not the object
        delendum = self.delendum.execute(world)
        assert isinstance(delendum, Object)
        world.delete(delendum.get_name())
        return Bool(value=True)

    def get_vars(self) -> List['Var']:
        return self.delendum.get_vars()

    def subst(self, dictionary: 'Ast') -> 'Ast':

        return Del(
            delendum=self.delendum.subst(dictionary),
            meta_info = self.meta_info,
        )
