from dataclasses import dataclass
from typing import List
from core.Ast import Ast
from typing import TYPE_CHECKING, Dict, List

if  TYPE_CHECKING:
    from core.World import World

@dataclass(frozen=True)
class Var(Ast):
    name:str

    def get_vars(self) -> List['Var']:
        return [self]

    def subst(self, d: Dict['Ast', 'Ast']) -> 'Ast':
        return d.get(self, self)

    def execute(self, world: 'World') -> 'Ast':
        return world.get_obj(self.name)
