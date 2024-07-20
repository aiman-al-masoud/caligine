from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional
from core.Ast import Ast
from core.MetaInfo import MetaInfo
from core.Halt import Halt

if TYPE_CHECKING:
    from core.World import World

@dataclass(kw_only=True)
class Exit(Ast):

    meta_info:Optional[MetaInfo]=field(default=None, compare=False)

    def execute(self, world: 'World') -> 'Ast':

        raise Halt(self, '', is_error=False)

    def subst(self, dictionary: 'Ast') -> 'Ast':

        return Exit(
            meta_info=self.meta_info,
        )
