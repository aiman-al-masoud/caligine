from dataclasses import dataclass
from core.Const import Const
from core.Ast import Ast

@dataclass
class Bool(Const):
    value:bool

    def __bool__(self):
        return self.value

    def perform_op(self, op: str, other: 'Ast') -> 'Ast':

        match op:
            case 'and': return self and other
            case 'or': return self or other
            case '==': return Bool(self == other)
            case '!=': return Bool(self != other)
        
        raise Exception()