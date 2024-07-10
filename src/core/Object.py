from dataclasses import dataclass
from typing import Dict
from canvas import Canvas
from core.Ast import Ast
from typing import TYPE_CHECKING, Dict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.World import World

@dataclass
class Object(Ast):
    name:str
    props: Dict[str, Ast]

    def execute(self, world: 'World') -> 'Ast':

        if not world.has_obj(self.name):
            world.add_obj(self)
            
        return self

    def subst(self, d: Dict['Ast', 'Ast']) -> 'Ast':
        return Object(self.name, {k:v.subst(d) for k,v in self.props.items()})

    def get(self, key: str) -> 'Ast':
        from core.Bool import Bool
        return self.props.get(key, Bool(False))

    def set(self, key: str, value: 'Ast'):
        self.props[key] = value
    
    def draw(self, canvas: Canvas):
        pass
