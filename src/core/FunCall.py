from dataclasses import dataclass
from typing import List
from core.Ast import Ast
from typing import TYPE_CHECKING, List

from core.Object import Object

if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var

@dataclass
class FunCall(Ast):
    fun_name:str
    args:List[Ast]

    def execute(self, world: 'World') -> 'Ast':
        
        for definition in world.defs:
            
            if not definition.matches(self):
                continue

            d = dict(zip(definition.args, self.args))
            body = definition.body.subst(Object('', d))
            return body.execute(world)
        
        raise Exception(f'Function {self.fun_name} is not defined.')

    def get_vars(self) -> List['Var']:
        return [v for x in self.args for v in x.get_vars()]

    def subst(self, dictionary: 'Ast') -> 'Ast':
        return FunCall(self.fun_name, [x.subst(dictionary) for x in self.args])
