from dataclasses import dataclass
from typing import List
from core.Ast import Ast
from typing import Dict, List


@dataclass(frozen=True)
class Var(Ast):
    name: str

    def get_vars(self) -> List['Var']:
        return [self]

    def subst(self, d: Dict['Ast', 'Ast']) -> 'Ast':
        return d.get(self, self)
