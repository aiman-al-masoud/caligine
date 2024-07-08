from dataclasses import dataclass
from typing import Dict
from core.Ast import Ast

from typing import TYPE_CHECKING, Dict, List


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core.World import World

@dataclass
class Object(Ast):
    name:str
    type:str
    kwargs: Dict[str, Ast]

    def execute(self, world: 'World') -> 'Ast':
        world.add_obj(self)
        return self

    def subst(self, d: Dict['Ast', 'Ast']) -> 'Ast':
        return Object(self.name, self.type, {k:v.subst(d) for k,v in self.kwargs.items()})

    def get(self, key: str) -> 'Ast':
        return self.kwargs[key]
