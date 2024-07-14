from core.Ast import Ast

class Panic(Exception):

    def __init__(self, panicked_ast:Ast, message:str) -> None:

        self.panicked_ast = panicked_ast
        meta = self.panicked_ast.get_meta_info()
        line = meta.line
        column = meta.column
        full_message = f'Error: {message} at: line={line} column={column}\n'
        super().__init__(full_message)

    def is_shorcircuit_binop(self, op: str) -> bool:
        return True        
