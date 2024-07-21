
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional
from core.Ast import Ast
from core.Bool import Bool
from core.MetaInfo import MetaInfo

if TYPE_CHECKING:
    from core.World import World


@dataclass(kw_only=True)
class Print(Ast):

    printandum: Ast
    meta_info: Optional[MetaInfo] = field(default=None, compare=False)

    def execute(self, world: 'World') -> 'Ast':

        world.stdout.write(str(self.printandum.execute(world))+'\n')
        world.stdout.flush()
        return Bool(value=True)

    def subst(self, dictionary: 'Ast') -> 'Ast':

        return Print(
            printandum=self.printandum.subst(dictionary),
            meta_info = self.meta_info,
        )
