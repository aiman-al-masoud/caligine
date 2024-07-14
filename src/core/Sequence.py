from dataclasses import dataclass, field
from typing import TYPE_CHECKING, List, Optional
from core.Ast import Ast
from core.Bool import Bool
from core.MetaInfo import MetaInfo

if TYPE_CHECKING:
    from core.World import World

@dataclass(kw_only=True)
class Sequence(Ast):

    values:List['Ast']
    meta_info: Optional[MetaInfo] = field(default=None, compare=False)

    def get_values(self):
        return self.values[:]
    
    def execute(self, world: 'World') -> 'Ast':
        return Sequence(values=[v.execute(world) for v in self.values])

    def __str__(self) -> str:
        return '[' + ','.join([str(v) for v in self.values]) + ']'

    def perform_op(self, op: str, other: 'Ast') -> 'Ast':

        match op:
            case '==': return Bool(value=self == other)
            case '!=': return Bool(value=self != other)
        
        from core.Panic import Panic
        raise Panic(self, f'unsupported operation {self} {op} {other}')

        