from dataclasses import dataclass
from typing import List
from core.Ast import Ast
from core.Bool import Bool
from typing import TYPE_CHECKING, List


if TYPE_CHECKING:
    from core.World import World


@dataclass
class Def(Ast):
    name:str
    args:List[Ast]
    body:Ast

    def execute(self, world: 'World') -> 'Ast':
        world.add_def(self)

        return Bool(True)

