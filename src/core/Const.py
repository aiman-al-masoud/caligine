from dataclasses import dataclass, field
from core.Ast import Ast
from typing import TYPE_CHECKING, List, Optional
from core.MetaInfo import MetaInfo

if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var


@dataclass(frozen=True, kw_only=True)
class Const(Ast):

    meta_info: Optional[MetaInfo] = field(default=None, compare=False)

    def execute(self, world: 'World') -> 'Ast':
        return self

    def get_vars(self) -> List['Var']:
        return []

    def subst(self, dictionary: 'Ast') -> 'Ast':
        return self
