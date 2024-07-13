from dataclasses import dataclass
from typing import List
from core.Ast import Ast
from typing import Dict, List


@dataclass(frozen=True)
class Var(Ast):
    name: str

    def get_vars(self) -> List['Var']:
        return [self]

    def subst(self, dictionary: 'Ast') -> 'Ast':
        return dictionary.get(self, self)
    
    def __str__(self) -> str:
        return self.name.upper()
