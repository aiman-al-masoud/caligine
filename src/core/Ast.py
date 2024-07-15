from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var

class Ast:

    def execute(self, world:'World') -> 'Ast':
        raise Exception()
    
    def subst(self, dictionary: 'Ast') -> 'Ast':
        raise Exception()

    def set(self, key:'str|Ast', value:'Ast'):
        raise Exception()

    def init(self, world:'World')->'Ast':
        return self

    def get(self, key:'str|Ast', default:'Ast|None'=None)->'Ast':
        raise Exception()

    def is_shorcircuit_binop(self, op:str)->bool:
        return False

    def perform_op(self, op:str, other:'Ast')->'Ast':
        raise Exception()

    def __int__(self)->int:
        raise Exception()
    
    def get_vars(self)->List['Var']:
        raise Exception()
