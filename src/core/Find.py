from dataclasses import dataclass
from itertools import combinations
from typing import TYPE_CHECKING
from core.Ast import Ast
from core.Object import Object
from core.Sequence import Sequence

if TYPE_CHECKING:
    from core.World import World

@dataclass
class Find(Ast):

    formula:Ast

    def execute(self, world: 'World') -> 'Sequence':

        vars = self.formula.get_vars()
        consts = world.get_objs()
        const_combos = combinations(consts, r=len(vars)) 
        assignments = (zip(vars, p) for p in const_combos)
        assignments_ok = []

        for a in assignments:
            
            a = dict(a)
            o = Object('', a) # pyright:ignore
            ast_concrete = self.formula.subst(o)

            if ast_concrete.execute(world):
                assignments_ok.append(o)

        return Sequence(assignments_ok)

