from dataclasses import dataclass
from typing import Dict
from core.Ast import Ast
from typing import TYPE_CHECKING, Dict
from typing import TYPE_CHECKING
from core.Str import Str
from core.Bool import Bool

if TYPE_CHECKING:
    from core.World import World

@dataclass
class Object(Ast):
    name:str
    props: Dict[Ast, Ast]

    def execute(self, world: 'World') -> 'Ast':
        return self

    def subst(self, dictionary: 'Ast') -> 'Ast':

        return Object(self.name, {k:v.subst(dictionary) for k,v in self.props.items()})

    def get(self, key: 'str|Ast', default:'Ast|None'=None) -> 'Ast':

        key = key if isinstance(key, Ast) else Str(key)
        return self.props.get(key, default if default else Bool(False))

    def set(self, key: 'str|Ast', value: 'Ast'):

        key = key if isinstance(key, Ast) else Str(key)
        self.props[key] = value
