
from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict, List
from core.Ast import Ast

if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var

@dataclass
class Asgn(Ast):
    owner:Ast
    key:str
    value:Ast

    def execute(self, world: 'World') -> 'Ast':

        owner = self.owner.execute(world)
        value = self.value.execute(world)
        owner.set(self.key, value)
        return self.value

    def get_vars(self) -> List['Var']:
        return self.owner.get_vars()+self.value.get_vars()

    def subst(self, d: Dict['Ast', 'Ast']) -> 'Ast':
        return Asgn(self.owner.subst(d), self.key, self.value.subst(d))
