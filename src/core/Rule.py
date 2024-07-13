from dataclasses import dataclass
from core.Ast import Ast
from typing import TYPE_CHECKING
from core.Find import Find
from core.Bool import Bool

if TYPE_CHECKING:
    from core.World import World

@dataclass
class Rule(Ast):
    condition:Ast
    consequence:Ast

    def execute(self, world: 'World') -> 'Ast':

        world.add_rule(self)
        return Bool(True)

    def apply(self, world:'World'):

        for d in Find(self.condition).execute(world).get_values():

            consequence = self.consequence.subst(d)
            consequence.execute(world)

        return Bool(True)
    
