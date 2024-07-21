from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional
from core.Ast import Ast
from core.Bool import Bool
from core.MetaInfo import MetaInfo
from core.Halt import Halt

if TYPE_CHECKING:
    from core.World import World

@dataclass(kw_only=True)
class Assert(Ast):

    assertion:Ast
    meta_info:Optional[MetaInfo]=field(default=None, compare=False)

    def execute(self, world: 'World') -> 'Ast':
        
        if not self.assertion.execute(world):
            raise Halt(self, f'assertion failed')
        
        return Bool(value=True)

    def subst(self, dictionary: 'Ast') -> 'Ast':

        return Assert(
            assertion=self.assertion.subst(dictionary), 
            meta_info=self.meta_info,
        )
