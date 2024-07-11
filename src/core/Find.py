from dataclasses import dataclass
from itertools import product
from typing import TYPE_CHECKING
from core.Ast import Ast
from core.Sequence import Sequence

if TYPE_CHECKING:
    from core.World import World

@dataclass
class Find(Ast):

    formula:Ast

    def execute(self, world: 'World') -> 'Sequence':

        vars = self.formula.get_vars()
        consts = world.get_objs()
        const_perms = product(consts, repeat=len(vars)) 
        assignments = (zip(vars, p) for p in const_perms)
        assignments_ok = []

        for a in assignments:
            
            a = dict(a)

            # no repeated individuals
            if len({v.name for v in a.values()}) != len(a.values()):
                continue

            ast_concrete = self.formula.subst(a) # pyright:ignore

            if ast_concrete.execute(world):
                assignments_ok.append(a)

        return Sequence(assignments_ok)

