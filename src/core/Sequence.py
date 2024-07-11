from dataclasses import dataclass
from typing import TYPE_CHECKING, List
from core.Ast import Ast
from core.Bool import Bool

if TYPE_CHECKING:
    from core.World import World

@dataclass
class Sequence(Ast):

    values:List['Ast']

    def get_values(self):
        return self.values[:]
    
    def execute(self, world: 'World') -> 'Ast':
        return Sequence([v.execute(world) for v in self.values])

    def __str__(self) -> str:
        return '[' + ','.join([str(v) for v in self.values]) + ']'

    def perform_op(self, op: str, other: 'Ast') -> 'Ast':

        match op:
            case '==': return Bool(self == other)
        
        raise Exception()