from dataclasses import dataclass
from core.Const import Const
from core.Ast import Ast
from core.Bool import Bool

@dataclass(frozen=True)
class Num(Const):
    value:float

    def perform_op(self, op: str, other: 'Ast') -> 'Ast':

        from core.Panic import Panic

        if not isinstance(other, Num):
            return Panic(self, 'number only supports operations with other numbers')

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

        return Panic(self, f'unsupported operation {self} {op} {other}')
    
    def __int__(self):
        return int(self.value)

    def __str__(self) -> str:
        return str(self.value)
