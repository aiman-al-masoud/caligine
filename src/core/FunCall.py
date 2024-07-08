from dataclasses import dataclass
from typing import List
from core.Ast import Ast


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var

from typing import TYPE_CHECKING, Dict, List


@dataclass
class FunCall(Ast):
    fun_name:str
    args:List[Ast]

    def execute(self, world: 'World') -> 'Ast':
        
        for definition in world.defs:
            
            if self.fun_name != definition.name:
                continue

            d = dict(zip(definition.args, self.args))
            body = definition.body.subst(d)
            return body.execute(world)
        
        raise Exception()

    def get_vars(self) -> List['Var']:
        return [v for x in self.args for v in x.get_vars()]

    def subst(self, d: Dict['Ast', 'Ast']) -> 'Ast':
        return FunCall(self.fun_name, [x.subst(d) for x in self.args])