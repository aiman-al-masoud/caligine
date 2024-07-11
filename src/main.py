#!/bin/python
import os
import sys
from core.Ast import Ast
from parse import Parser
from core.World import World
from app import app, start_update_screen

parser = Parser()
world = World([], [], [])

path_script = os.path.abspath(sys.argv[1]) 
world.set_path_script(path_script)
text = open(path_script).read()
ast = parser.parse(text)

assert isinstance(ast, Ast)
ast.execute(world)

world.start()
app.config['world'] = world

start_update_screen(world)

app.run(host='0.0.0.0', port=8000)


