from dataclasses import dataclass, field
from itertools import combinations
from typing import TYPE_CHECKING, Optional
from core.Ast import Ast
from core.MetaInfo import MetaInfo
from core.Object import Object
from core.Sequence import Sequence

if TYPE_CHECKING:
    from core.World import World


@dataclass(kw_only=True)
class Find(Ast):

    formula: Ast
    meta_info: Optional[MetaInfo] = field(default=None, compare=False)

    def execute(self, world: 'World') -> 'Sequence':

        vars = self.formula.get_vars()
        consts = world.values()
        const_combos = combinations(consts, r=len(vars))
        assignments = (zip(vars, p) for p in const_combos)
        assignments_ok = []

        for a in assignments:

            a = dict(a)
            o = Object(props=a)  # pyright:ignore
            ast_concrete = self.formula.subst(o)

            if ast_concrete.execute(world):
                assignments_ok.append(o)

        return Sequence(
            values=assignments_ok, 
            meta_info = self.meta_info,
        )
    
    def subst(self, dictionary: 'Ast') -> 'Ast':

        return Find(
            formula=self.formula.subst(dictionary),
            meta_info=self.meta_info,
        )
