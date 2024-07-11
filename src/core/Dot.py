from dataclasses import dataclass
from core.Ast import Ast
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var

@dataclass
class Dot(Ast):
    owner:Ast
    key:str

    def execute(self, world: 'World') -> 'Ast':
        
        owner = self.owner.execute(world)
        return owner.get(self.key).execute(world)

    def get_vars(self) -> List['Var']:
        return self.owner.get_vars()
    
    def subst(self, dictionary: 'Ast') -> 'Ast':
        return Dot(self.owner.subst(dictionary), self.key)
