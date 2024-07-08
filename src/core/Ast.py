from itertools import product
from typing import TYPE_CHECKING, Dict, List, cast

if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var


class Ast:

    def execute(self, world:'World') -> 'Ast':
        raise Exception()

    def subst(self, d: Dict['Ast', 'Ast']) -> 'Ast':
        raise Exception()

    def set(self, key:str, value:'Ast'):
        raise Exception()

    def get(self, key:str)->'Ast':
        raise Exception()

    def perform_op(self, op:str, other:'Ast')->'Ast':
        raise Exception()

    def get_vars(self)->List['Var']:
        raise Exception()

    def find(self, world:'World'): #-> List[Dict['Ast', 'Ast']]:
        
        vars = cast(List[Ast], self.get_vars())
        consts = cast(List[Ast],world.get_obj_ids())
        const_perms = product(consts, repeat=len(vars)) 
        const_perms = set(const_perms)
        assignments = [dict(zip(vars, p)) for p in const_perms]
        # assignments_ok:List[Dict['Ast', 'Ast']] = []

        for a in assignments:
            ast_concrete = self.subst(a)
            
            if ast_concrete.execute(world):
                yield a
                # assignments_ok.append(a)
        
        # return assignments_ok
