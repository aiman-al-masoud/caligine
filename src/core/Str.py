from dataclasses import dataclass
from core.Const import Const
from core.Ast import Ast
from core.Bool import Bool

@dataclass(frozen=True, kw_only=True)
class Str(Const):
    value:str
    
    def perform_op(self, op: str, other: 'Ast') -> 'Ast':

        match op:
            case '==': return Bool(value=self == other)
            case '!=': return Bool(value=self != other)

        from core.Panic import Panic
        raise Panic(self, f'unsupported operation {self} {op} {other}')
    
    def __str__(self):
        return self.value