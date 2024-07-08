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


