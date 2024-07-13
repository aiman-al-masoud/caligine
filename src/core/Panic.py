from dataclasses import dataclass
from core.Ast import Ast
from core.World import World


@dataclass
class Panic(Ast):
    
    panicked_ast:Ast
    message:str

    def execute(self, world: 'World') -> 'Ast':

        meta = self.panicked_ast.get_meta_info()
        line = meta.line
        column = meta.column
        world.stderr.write(f'Error: {self.message} at: line={line} column={column}\n')
        world.stderr.flush()
        return self

    def is_shorcircuit_binop(self, op: str) -> bool:
        return True        
