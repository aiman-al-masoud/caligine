from itertools import product
from typing import TYPE_CHECKING, Any, Dict, Generator, List



if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var


class Ast:

    def execute(self, world:'World') -> 'Ast':
        raise Exception()

    def subst(self, d: Dict['Ast', 'Ast']) -> 'Ast':
        raise Exception()

    def set(self, key:str, value:'Ast'):
        raise Exception(self.__class__)

    def get(self, key:str)->'Ast':
        raise Exception()

    def perform_op(self, op:str, other:'Ast')->'Ast':
        raise Exception()

    def get_vars(self)->List['Var']:
        raise Exception()

    # def draw(self, canvas:Canvas):
    #     raise Exception()

    def __int__(self)->int:
        raise Exception()

    def find(self, world:'World') -> Generator[Dict['Ast', 'Ast'], Any, None]:

        vars = self.get_vars()
        
        vars = []  # TODO!!!!   PUT BACK prolog-like SYSTEM OF VARs VS IDs

        consts = world.get_objs()
        const_perms = product(consts, repeat=len(vars)) 
        assignments = (zip(vars, p) for p in const_perms)

        for a in assignments:
            
            a = dict(a)

            # no repeated individuals
            if len({v.name for v in a.values()}) != len(a.values()):
                continue

            ast_concrete = self.subst(a) # pyright:ignore

            x = ast_concrete.execute(world)
            if x:

                yield a # pyright:ignore

