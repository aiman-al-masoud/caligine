#!/bin/python
import sys
from lark import Lark
from core.Ast import Ast
from parse import ToAst
from core.World import World

parser = Lark(
    grammar=open('grammar.lark').read(), 
    ambiguity='explicit', 
    lexer='basic',
)
toast = ToAst()
world = World([], [], [])
text = open(sys.argv[1]).read()
st = parser.parse(text)
ast = toast.transform(st)


# print(ast)
# exit()


assert isinstance(ast, Ast)
ast.execute(world)


