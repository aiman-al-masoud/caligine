#!/bin/python
import sys
from canvas import Canvas
from core.Ast import Ast
from core.Client import Client
from parse import Parser
from core.World import World
from app import app

parser = Parser()
world = World([], [], [])
text = open(sys.argv[1]).read()
ast = parser.parse(text)

assert isinstance(ast, Ast)
ast.execute(world)


canvas = Canvas(500, 500, 'white')
world.start()
app.config['world'] = world
app.run(host='0.0.0.0', port=8000)


