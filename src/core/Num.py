from dataclasses import dataclass
from core.Const import Const
from core.Ast import Ast

@dataclass
class Num(Const):
    value:float

    def perform_op(self, op: str, other: 'Ast') -> 'Ast':

        from core.Bool import Bool

        if not isinstance(other, Num):
            return Bool(False)

        match op:
            case '+': return Num(self.value + other.value)
            case '-': return Num(self.value - other.value)
            case '*': return Num(self.value * other.value)
            case '/': return Num(self.value / other.value)
            case '>': return Bool(self.value > other.value)
            case '<': return Bool(self.value < other.value)
            case '>=': return Bool(self.value >= other.value)
            case '<=': return Bool(self.value <= other.value)
            case '==': return Bool(self.value == other.value)
            case '!=': return Bool(self.value != other.value)

        raise Exception()
    
    def __int__(self):
        return int(self.value)




    