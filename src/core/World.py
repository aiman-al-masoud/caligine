from dataclasses import dataclass, field
from re import L
from typing import List, Literal
from core.Def import Def
from core.Rule import Rule
from core.Object import Object
from queue import Queue

from core.Str import Str

@dataclass
class World:
    objs:List['Object']
    defs:List['Def']
    rules:List['Rule']
    event_queue:Queue['KeyEvent'] = field(default_factory=lambda: Queue())

    def add_def(self, d:Def):
        self.defs.append(d)

    def add_rule(self, r:Rule):
        self.rules.append(r)
    
    def add_obj(self, o:Object):
        self.objs.append(o)

    def rm_obj(self, name:str):
        self.objs = [x for x in self.objs if x.name != name]

    def has_obj(self, name:str):
        return bool([x for x in self.objs if x.name == name])

    def get_obj(self, name:str):
        
        if not self.has_obj(name):
            raise Exception(f'"{name}" does not exist')
            
        return [x for x in self.objs if x.name == name][0]
    
    def get_objs(self):
        return self.objs

    def tick(self):

        for rule in self.rules:
            rule.apply(self)

    def print(self, msg:str):
        print(msg)

    def error(self, msg:str):
        raise Exception(msg)

    def put_event(self, e:'KeyEvent'):
        self.event_queue.put(e)
    
    def process_event_queue(self):

        while not self.event_queue.empty():
            e = self.event_queue.get()
            client = self.get_obj(e.client_id).execute(self)
            client.get('keyboard').execute(self).set(e.key, Str(e.state))


@dataclass
class KeyEvent:
    client_id: str
    key:str
    state:Literal['up', 'down']

