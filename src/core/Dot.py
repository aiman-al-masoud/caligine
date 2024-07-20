from dataclasses import dataclass, field
from core.Ast import Ast
from typing import TYPE_CHECKING, List, Optional

from core.MetaInfo import MetaInfo

if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var

@dataclass(kw_only=True)
class Dot(Ast):

    owner:Ast
    key:str
    meta_info: Optional[MetaInfo] = field(default=None, compare=False)


    def execute(self, world: 'World') -> 'Ast':
        
        owner = self.owner.execute(world)
        return owner.get(self.key).execute(world)

    def get_vars(self) -> List['Var']:
        return self.owner.get_vars()
    
    def subst(self, dictionary: 'Ast') -> 'Ast':

        return Dot(
            owner=self.owner.subst(dictionary), 
            key=self.key,
            meta_info = self.meta_info,
        )
