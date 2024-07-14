from dataclasses import dataclass, field
from typing import List, Optional
from core.Ast import Ast
from core.Bool import Bool
from typing import TYPE_CHECKING, List
from core.FunCall import FunCall
from core.MetaInfo import MetaInfo

if TYPE_CHECKING:
    from core.World import World


@dataclass(kw_only=True)
class Def(Ast):

    name: str
    args: List[Ast]
    body: Ast
    meta_info: Optional[MetaInfo] = field(default=None, compare=False)

    def execute(self, world: 'World') -> 'Ast':

        world.add_def(self)
        return Bool(value=True)

    def matches(self, fun_call: FunCall):

        return self.name == fun_call.fun_name
