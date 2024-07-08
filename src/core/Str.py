from dataclasses import dataclass
from core.Const import Const
from core.Ast import Ast


@dataclass
class Str(Const):
    value:str
    
    def perform_op(self, op: str, other: 'Ast') -> 'Ast':

        from core.Bool import Bool

        match op:
            case '==': return Bool(self == other)
            case '!=': return Bool(self != other)

        raise Exception()