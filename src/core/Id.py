from dataclasses import dataclass, field
from typing import TYPE_CHECKING, List, Optional
from core.Ast import Ast
from core.MetaInfo import MetaInfo
from core.Var import Var

if TYPE_CHECKING:
    from core.World import World


@dataclass(kw_only=True)
class Id(Ast):

    name: str
    meta_info: Optional[MetaInfo] = field(default=None, compare=False)

    def execute(self, world: 'World') -> 'Ast':

        object = world.get_obj(self.name)

        if object is None:
            from core.Panic import Panic
            raise Panic(self, f'the object {self.name} is not defined')

        return object

    def subst(self, dictionary: 'Ast') -> 'Ast':
        return self

    def get_vars(self) -> List['Var']:
        return []
