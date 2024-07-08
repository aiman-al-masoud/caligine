#!/bin/python
import sys
from time import sleep
from core.Ast import Ast
from parse import Parser
from core.World import World
from threading import Thread

parser = Parser()
world = World([], [], [])
text = open(sys.argv[1]).read()
ast = parser.parse(text)

assert isinstance(ast, Ast)
ast.execute(world)


def game_loop():
    
    while True:

        sys.stdout.write(str(world.event_queue.qsize())+'\n')
        sys.stdout.flush()

        world.process_event_queue()
        world.tick()
        
        sleep(0.1)

Thread(target=game_loop).start()


from app import app
app.config['world'] = world
app.run(host='0.0.0.0', port=8000)

# xs = list(parser.parse('coincide(x, y)').find(world))
# xs = [{k.name:v.name for k,v in x.items()} for x in xs]
# print(xs)


