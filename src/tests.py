import os
from core.World import World
from parse import Parser


def test_move_eat():

    parser = Parser()
    path = os.path.split(os.path.abspath(__file__))[0]+'/examples/example2.txt'
    text = open(path).read()
    world = World([], [], [])
    world.set_path_script(path)
    print(text)
    ast = parser.parse(text)
    ast.execute(world)




