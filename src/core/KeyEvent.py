
from dataclasses import dataclass
from typing import Literal
from core.Ast import Ast
from core.Str import Str
from core.World import World
from core.Bool import Bool

@dataclass(kw_only=True)
class KeyEvent(Ast):
    
    client_id: str
    key:str
    state:Literal['up', 'down']

    def execute(self, world: 'World') -> 'Ast':

        client = world.get_client(self.client_id)
        
        if not client:
            raise Exception()

        client.get('keyboard').execute(world).set(self.key, Str(value=self.state))
        return Bool(value=True)

