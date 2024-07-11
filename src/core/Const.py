from dataclasses import dataclass
from core.Ast import Ast
from typing import TYPE_CHECKING, Dict, List


if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var

@dataclass(frozen=True)
class Const(Ast):
    
    def execute(self, world: 'World') -> 'Ast':
        return self

    def get_vars(self) -> List['Var']:
        return []

    def subst(self, dictionary: 'Ast') -> 'Ast':
        return self