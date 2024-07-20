from dataclasses import dataclass, field
from core.Ast import Ast
from core.Bool import Bool
from typing import TYPE_CHECKING, List, Optional

from core.MetaInfo import MetaInfo

if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var


@dataclass(kw_only=True)
class Not(Ast):

    negated:Ast
    meta_info: Optional[MetaInfo] = field(default=None, compare=False)


    def execute(self, world: 'World') -> 'Ast':

        ast = self.negated.execute(world)
        return Bool(value=not bool(ast))
 
    def get_vars(self) -> List['Var']:
        return self.negated.get_vars()

    def subst(self, dictionary: 'Ast') -> 'Ast':

        return Not(
            negated=self.negated.subst(dictionary),
            meta_info = self.meta_info,
        )
