#!/bin/python
import sys
from canvas import Canvas
from core.Ast import Ast
from parse import Parser
from core.World import World
from app import app, start_update_screen

parser = Parser()
world = World([], [], [])
text = open(sys.argv[1]).read()
ast = parser.parse(text)

assert isinstance(ast, Ast)
ast.execute(world)


world.start()
app.config['world'] = world

start_update_screen(world)

app.run(host='0.0.0.0', port=8000)


