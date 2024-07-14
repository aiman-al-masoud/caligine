from dataclasses import dataclass, field
from typing import List, Optional
from core.Ast import Ast
from core.MetaInfo import MetaInfo


@dataclass(frozen=True, kw_only=True)
class Var(Ast):

    name: str
    meta_info: Optional[MetaInfo] = field(default=None, compare=False)

    def get_vars(self) -> List['Var']:
        return [self]

    def subst(self, dictionary: 'Ast') -> 'Ast':
        return dictionary.get(self, self)

    def __str__(self) -> str:
        return self.name.upper()
