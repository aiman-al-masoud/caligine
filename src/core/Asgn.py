
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, List, Optional
from core.Ast import Ast
from core.MetaInfo import MetaInfo

if TYPE_CHECKING:
    from core.World import World
    from core.Var import Var


@dataclass(kw_only=True)
class Asgn(Ast):

    owner: Ast
    key: str
    value: Ast
    meta_info: Optional[MetaInfo] = field(default=None, compare=False)

    def execute(self, world: 'World') -> 'Ast':

        owner = self.owner.execute(world)
        value = self.value.execute(world)
        owner.set(self.key, value)
        return self.value

    def get_vars(self) -> List['Var']:
        return self.owner.get_vars()+self.value.get_vars()

    def subst(self, dictionary: 'Ast') -> 'Ast':
        return Asgn(owner=self.owner.subst(dictionary), key=self.key, value=self.value.subst(dictionary))
