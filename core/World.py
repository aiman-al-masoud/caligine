from dataclasses import dataclass
from typing import List
from core.Def import Def
from core.Rule import Rule
from core.Object import Object

@dataclass
class World:
    objs:List['Object']
    defs:List['Def']
    rules:List['Rule']

    def add_def(self, d:Def):
        self.defs.append(d)

    def add_rule(self, r:Rule):
        self.rules.append(r)
    
    def add_obj(self, o:Object):
        self.objs.append(o)

    def rm_obj(self, name:str):
        self.objs = [x for x in self.objs if x.name != name]

    def get_obj(self, name:str):
        return [x for x in self.objs if x.name == name][0]
    
    def get_obj_ids(self):
        from core.Id import Id
        return [Id(x.name) for x in self.objs]

    def tick(self):

        for rule in self.rules:
            rule.apply(self)

    def print(self, msg:str):
        print(msg)

