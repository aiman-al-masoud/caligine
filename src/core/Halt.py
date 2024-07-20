from core.Ast import Ast


class Halt(Exception):

    def __init__(
        self,
        panicked_ast: Ast | None = None,
        message: str = '',
        is_error=True,
    ) -> None:

        self.panicked_ast = panicked_ast
        self.is_error = is_error
        meta = self.panicked_ast.get_meta_info() if self.panicked_ast else None
        line = meta.line if meta else 'unknown'
        column = meta.column if meta else 'unknown'
        self.full_message = f'Halt: {message}, at line={line} column={column}\n'
        super().__init__(self.full_message)

    def is_shorcircuit_binop(self, op: str) -> bool:
        return True
