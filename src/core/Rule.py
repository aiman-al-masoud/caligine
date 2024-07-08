from dataclasses import dataclass
from core.Ast import Ast
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.World import World


@dataclass
class Rule(Ast):
    condition:Ast
    consequence:Ast

    def execute(self, world: 'World') -> 'Ast':

        from core.Bool import Bool
        world.add_rule(self)
        return Bool(True)

    def apply(self, world:'World'):

        for d in self.condition.find(world):
            consequence = self.consequence.subst(d)
            consequence.execute(world)

        from core.Bool import Bool
        return Bool(True)
    
