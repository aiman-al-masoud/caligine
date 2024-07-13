import os
from core.World import World
from parse import Parser
from core.Sequence import Sequence


def test_move_eat():

    parser = Parser()
    path = os.path.split(os.path.abspath(__file__))[0]+'/examples/example2.txt'
    text = open(path).read()
    world = World()
    world.set_path_script(path)
    ast = parser.parse(text)
    ast.execute(world)

    find_sprites = parser.parse('find X.type == "sprite"')
    sprites_before = find_sprites.execute(world)

    while parser.parse('trump.score < 3').execute(world):
        world.tick()

    sprites_after = find_sprites.execute(world)
    assert int(parser.parse('trump.score').execute(world)) == 3
    assert isinstance(sprites_before, Sequence)
    assert isinstance(sprites_after, Sequence)
    assert len(sprites_before.get_values()) == 4
    assert len(sprites_after.get_values()) == 1



