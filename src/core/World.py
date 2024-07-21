from dataclasses import dataclass, field
import sys
from typing import TYPE_CHECKING, Dict, List, TextIO
from core.Bool import Bool
from core.Def import Def
from core.Rule import Rule
from queue import Queue
from time import sleep
from core.Ast import Ast
from core.Str import Str

if TYPE_CHECKING:
    from core.KeyEvent import KeyEvent


@dataclass(kw_only=True)
class World(Ast):

    props: Dict[Ast, Ast] = field(default_factory=lambda: {})
    defs: List['Def'] = field(default_factory=lambda: [])
    rules: List['Rule'] = field(default_factory=lambda: [])
    event_queue: Queue['KeyEvent'] = field(default_factory=lambda: Queue())
    stdout:TextIO = sys.stdout

    def copy(self):
        
        return World(
            props = self.props.copy(),
            defs = self.defs.copy(),
            rules = self.rules.copy(),
            event_queue = Queue(),
            stdout=self.stdout,
        )

    def values(self):
        return self.props.values()

    def set(self, key:'str|Ast', value:'Ast'):

        if value not in self.values():
            value.init(self)

        key = key if isinstance(key, Ast) else Str(value=key)
        self.props[key] = value

    def get(self, key:'str|Ast', default:'Ast|None'=None)->'Ast':
        
        key = key if isinstance(key, Ast) else Str(value=key)

        if key == Str(value='world'):
            return self

        return self.props.get(key, default if default is not None else Bool(value=False, meta_info=key.get_meta_info()))

    def delete(self, key:'str|Ast'):

        key = key if isinstance(key, Ast) else Str(value=key)
        del self.props[key]

    def has(self, key: 'str|Ast'):

        key = key if isinstance(key, Ast) else Str(value=key)
        return key in self.props

    def add_def(self, d: Def):
        self.defs.append(d)

    def add_rule(self, r: Rule):
        self.rules.append(r)

    def tick(self):

        for rule in self.rules:
            rule.apply(self)

    def put_event(self, e: 'KeyEvent'):
        self.event_queue.put(e)

    def process_event_queue(self):

        while not self.event_queue.empty():
            e = self.event_queue.get()
            e.execute(self)

    def game_loop(self):

        while True:

            self.process_event_queue()
            self.tick()
            sleep(0.1)
