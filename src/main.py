#!/bin/python
import sys
from core.Ast import Ast
from parse import Parser
from core.World import World

parser = Parser()
world = World([], [], [])
text = open(sys.argv[1]).read()
ast = parser.parse(text)

assert isinstance(ast, Ast)
ast.execute(world)


# xs = list(parser.parse('coincide(x, y)').find(world))
# xs = [{k.name:v.name for k,v in x.items()} for x in xs]
# print(xs)


