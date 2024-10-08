from dataclasses import dataclass, field
from typing import TYPE_CHECKING, List, Optional
from core.Ast import Ast
from core.Bool import Bool
from core.MetaInfo import MetaInfo

if TYPE_CHECKING:
    from core.World import World


@dataclass(kw_only=True)
class Sequence(Ast):

    values: List['Ast']
    index = 0
    meta_info: Optional[MetaInfo] = field(default=None, compare=False)

    def execute(self, world: 'World') -> 'Ast':
        return Sequence(values=[v.execute(world) for v in self.values])

    def __str__(self) -> str:
        return '[' + ','.join([str(v) for v in self.values]) + ']'

    def perform_op(self, op: str, other: 'Ast') -> 'Ast':

        match op:
            case '==': return Bool(value=self == other)
            case '!=': return Bool(value=self != other)

        from core.Halt import Halt
        raise Halt(self, f'unsupported operation {self} {op} {other}')

    def __iter__(self):
        
        return self

    def __next__(self):

        self.index += 1

        try:
            return self.values[self.index-1]
        except IndexError:

            self.index = 0
            raise StopIteration
