from dataclasses import dataclass, field
import sys
from typing import TYPE_CHECKING, Dict, List, TextIO, Tuple
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
    canvas_size: Tuple[int, int] = (400, 400)
    canvas_bg_color: str = 'rgb(100, 100, 100)'
    path_script:str = ''
    stdout:TextIO = sys.stdout
    stderr:TextIO = sys.stderr

    def copy(self):
        
        return World(
            props = self.props.copy(),
            defs = self.defs.copy(),
            rules = self.rules.copy(),
            event_queue = Queue(),
            canvas_size = self.canvas_size,
            canvas_bg_color= self.canvas_bg_color,
            path_script=self.path_script,
            stdout=self.stdout,
            stderr=self.stderr,
        )

    def values(self):
        return self.props.values()

    def set(self, key:'str|Ast', value:'Ast'):

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

    def set_canvas_size(self, w: int, h: int):
        self.canvas_size = (w, h)

    def get_canvas_width(self):
        return self.canvas_size[0]

    def get_canvas_height(self):
        return self.canvas_size[1]

    def set_canvas_bg_color(self, canvas_bg_color):
        self.canvas_bg_color = canvas_bg_color

    def get_canvas_bg_color(self):
        return self.canvas_bg_color

    def set_path_script(self, path_script:str):
        self.path_script = path_script

    def get_path_script(self):
        return self.path_script
        