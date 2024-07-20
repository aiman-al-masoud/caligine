from dataclasses import dataclass, field
from typing import TYPE_CHECKING, List, Optional
from core.Ast import Ast
from core.Bool import Bool
from core.MetaInfo import MetaInfo
from core.Var import Var

if TYPE_CHECKING:
    from core.World import World


@dataclass(kw_only=True)
class Id(Ast):

    name: str
    meta_info: Optional[MetaInfo] = field(default=None, compare=False)

    def execute(self, world: 'World') -> 'Ast':

        return world.get(self.name, Bool(value=False, meta_info=self.get_meta_info()))

    def subst(self, dictionary: 'Ast') -> 'Ast':
        return self

    def get_vars(self) -> List['Var']:
        return []
