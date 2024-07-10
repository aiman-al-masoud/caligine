from dataclasses import dataclass, field
from threading import Thread
from typing import TYPE_CHECKING, List, Tuple
from core.Sprite import Sprite
from core.Client import Client
from core.Def import Def
from core.Rule import Rule
from core.Object import Object
from queue import Queue
from time import sleep
if TYPE_CHECKING:
    from core.KeyEvent import KeyEvent


@dataclass
class World:
    objs:List['Object']
    defs:List['Def']
    rules:List['Rule']
    event_queue:Queue['KeyEvent'] = field(default_factory=lambda: Queue())
    canvas_size: Tuple[int, int] = (300, 300)
    canvas_bg_color:str = 'white'

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
            e.execute(self)

    def game_loop(self):

        while True:

            self.process_event_queue()
            self.tick()            
            sleep(0.1)

    def start(self):
        Thread(target=self.game_loop).start()

    def get_clients(self):
        return [o for o in self.objs if isinstance(o, Client)]
    
    def get_client(self, name:str):
        
        clients = self.get_clients()
        client = [c for c in clients if c.name == name][0]
        return client

    def get_sprites(self):
        return [o for o in self.objs if isinstance(o, Sprite)]

    def set_canvas_size(self, w:int,h:int):
        self.canvas_size = (w, h)
    
    def get_canvas_width(self):
        return self.canvas_size[0]
    
    def get_canvas_height(self):
        return self.canvas_size[1]
    
    def set_canvas_bg_color(self, canvas_bg_color):
        self.canvas_bg_color = canvas_bg_color
    
    def get_canvas_bg_color(self):
        return self.canvas_bg_color
