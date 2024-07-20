from dataclasses import dataclass, field
from typing import List, Optional
from core.Ast import Ast
from typing import TYPE_CHECKING, List
from core.MetaInfo import MetaInfo
from core.Object import Object

if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var

@dataclass(kw_only=True)
class FunCall(Ast):
    fun_name:str
    args:List[Ast]
    meta_info: Optional[MetaInfo] = field(default=None, compare=False)

    def execute(self, world: 'World') -> 'Ast':
        
        for definition in world.defs:
            
            if not definition.matches(self):
                continue

            d = dict(zip(definition.args, self.args))
            body = definition.body.subst(Object(props= d))
            return body.execute(world)
        
        from core.Halt import Halt
        raise Halt(self, f'the function {self.fun_name} is not defined')

    def get_vars(self) -> List['Var']:
        return [v for x in self.args for v in x.get_vars()]

    def subst(self, dictionary: 'Ast') -> 'Ast':
        
        return FunCall(
            fun_name=self.fun_name, 
            args=[x.subst(dictionary) for x in self.args],
            meta_info = self.meta_info,
        )
