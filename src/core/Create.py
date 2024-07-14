from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional
from core.Ast import Ast
from core.MetaInfo import MetaInfo
from core.Object import Object

if TYPE_CHECKING:
    from core.World import World


@dataclass(kw_only=True)
class Create(Ast):

    creandum: Ast
    meta_info: Optional[MetaInfo] = field(default=None, compare=False)

    def execute(self, world: 'World') -> 'Ast':

        # TODO: Remove assertion. Assign rather than create-with-name
        assert isinstance(self.creandum, Object)
        self.creandum.init(world)
        world.add_obj(self.creandum)
        return self.creandum
