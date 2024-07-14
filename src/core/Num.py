from dataclasses import dataclass
from core.Const import Const
from core.Ast import Ast
from core.Bool import Bool

@dataclass(frozen=True, kw_only=True)
class Num(Const):
    value:float

    def perform_op(self, op: str, other: 'Ast') -> 'Ast':

        from core.Panic import Panic

        if not isinstance(other, Num):
            raise Panic(self, 'number only supports operations with other numbers')

        match op:
            case '+': return Num(value=self.value + other.value)
            case '-': return Num(value=self.value - other.value)
            case '*': return Num(value=self.value * other.value)
            case '/': return Num(value=self.value / other.value)
            case '>': return Bool(value=self.value > other.value)
            case '<': return Bool(value=self.value < other.value)
            case '>=': return Bool(value=self.value >= other.value)
            case '<=': return Bool(value=self.value <= other.value)
            case '==': return Bool(value=self.value == other.value)
            case '!=': return Bool(value=self.value != other.value)

        raise Panic(self, f'unsupported operation {self} {op} {other}')
    
    def __int__(self):
        return int(self.value)

    def __str__(self) -> str:
        return str(self.value)
