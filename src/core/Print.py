
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional
from core.Ast import Ast
from core.Bool import Bool
from core.MetaInfo import MetaInfo

if TYPE_CHECKING:
    from core.World import World


@dataclass(kw_only=True)
class Print(Ast):

    prindandum: Ast
    meta_info: Optional[MetaInfo] = field(default=None, compare=False)

    def execute(self, world: 'World') -> 'Ast':

        world.stdout.write(str(self.prindandum.execute(world))+'\n')
        world.stdout.flush()
        return Bool(value=True)

    def subst(self, dictionary: 'Ast') -> 'Ast':

        return Print(
            prindandum=self.prindandum.subst(dictionary),
            meta_info = self.meta_info,
        )
