from dataclasses import dataclass, field
from typing import TYPE_CHECKING, List, Optional
from core.Ast import Ast
from core.Bool import Bool
from core.MetaInfo import MetaInfo
from core.Panic import Panic

if TYPE_CHECKING:
    from core.World import World

@dataclass(kw_only=True)
class Prog(Ast):

    statements:List[Ast]
    meta_info: Optional[MetaInfo] = field(default=None, compare=False)

    def execute(self, world: 'World') -> 'Ast':
        
        res:Ast = Bool(value=False)

        for statement in self.statements:

            res = statement.execute(world)

            if isinstance(res, Panic):
                res.execute(world)
                return res
        
        return res

    def subst(self, dictionary: 'Ast') -> 'Ast':
        
        return Prog(statements=[s.subst(dictionary) for s in self.statements])
