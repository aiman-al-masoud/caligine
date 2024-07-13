from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict, List

from core.MetaInfo import MetaInfo

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

    def set_meta_info(self, meta_info:MetaInfo):

        self.meta_info = meta_info
        return self
    
    def get_meta_info(self)->MetaInfo:
        return self.meta_info
    
