from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict, List
from core.Ast import Ast
from core.Var import Var

if  TYPE_CHECKING:
    from core.World import World

@dataclass
class Id(Ast):
    name:str

    def execute(self, world: 'World') -> 'Ast':
        return world.get_obj(self.name)

    def subst(self, dictionary: 'Ast') -> 'Ast':
        return self

    def get_vars(self) -> List['Var']:
        return []
