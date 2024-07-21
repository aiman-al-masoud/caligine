from dataclasses import dataclass, field
from core.Ast import Ast
from typing import TYPE_CHECKING, Optional
from core.Find import Find
from core.Bool import Bool
from core.MetaInfo import MetaInfo

if TYPE_CHECKING:
    from core.World import World

@dataclass(kw_only=True)
class Rule(Ast):

    condition:Ast
    consequence:Ast
    meta_info: Optional[MetaInfo] = field(default=None, compare=False)

    def execute(self, world: 'World') -> 'Ast':

        world.add_rule(self)
        return Bool(value=True)

    def apply(self, world:'World'):

        for d in Find(formula=self.condition).execute(world):

            consequence = self.consequence.subst(d)
            consequence.execute(world)

        return Bool(value=True)
    
