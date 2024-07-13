from dataclasses import dataclass
from typing import TYPE_CHECKING, List
from core.Ast import Ast
from core.Var import Var

if  TYPE_CHECKING:
    from core.World import World

@dataclass
class Id(Ast):
    name:str

    def execute(self, world: 'World') -> 'Ast':

        object = world.get_obj(self.name)

        if object is None:
            from core.Panic import Panic
            return Panic(self, f'the object {self.name} is not defined')
        
        return object

    def subst(self, dictionary: 'Ast') -> 'Ast':
        return self

    def get_vars(self) -> List['Var']:
        return []
