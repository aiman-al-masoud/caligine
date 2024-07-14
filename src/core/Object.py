from dataclasses import dataclass, field
from typing import Dict, Optional
from core.Ast import Ast
from typing import TYPE_CHECKING, Dict
from typing import TYPE_CHECKING
from core.MetaInfo import MetaInfo
from core.Str import Str
from core.Bool import Bool

if TYPE_CHECKING:
    from core.World import World


@dataclass(kw_only=True)
class Object(Ast):

    name: str
    props: Dict[Ast, Ast]
    meta_info: Optional[MetaInfo] = field(default=None, compare=False)

    def init(self, world: 'World') -> 'Ast':

        self.set('type', Str(value='object'))
        return self

    def execute(self, world: 'World') -> 'Ast':
        return self

    def subst(self, dictionary: 'Ast') -> 'Ast':

        return Object(name=self.name, props={k: v.subst(dictionary) for k, v in self.props.items()})

    def get(self, key: 'str|Ast', default: 'Ast|None' = None) -> 'Ast':

        key = key if isinstance(key, Ast) else Str(value=key)
        return self.props.get(key, default if default else Bool(value=False))

    def set(self, key: 'str|Ast', value: 'Ast'):

        key = key if isinstance(key, Ast) else Str(value=key)
        self.props[key] = value

    def has(self, key: 'str|Ast'):

        key = key if isinstance(key, Ast) else Str(value=key)
        return key in self.props

    def __str__(self) -> str:
        return str({str(k): str(v) for k, v in self.props.items()})

    def perform_op(self, op: str, other: 'Ast') -> 'Ast':

        match op:
            case '==': return Bool(value=self == other)
            case '!=': return Bool(value=self != other)

        from core.Panic import Panic
        raise Panic(self, f'unsupported operation {self} {op} {other}')
