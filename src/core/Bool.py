from dataclasses import dataclass
from core.Const import Const
from core.Ast import Ast


@dataclass(frozen=True, kw_only=True)
class Bool(Const):
    value:bool

    def __bool__(self):
        return self.value

    def perform_op(self, op: str, other: 'Ast') -> 'Ast':

        match op:
            case 'and': return self and other
            case 'or': return self or other
            case '==': return Bool(value=self == other)
            case '!=': return Bool(value=self != other)
        
        return Bool(value=False)

    def is_shorcircuit_binop(self, op: str) -> bool:
        
        match op:
            case 'and': return not self
            case 'or': return bool(self)
        
        return False