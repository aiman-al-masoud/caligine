#!/bin/python
import os
import sys
from core.Ast import Ast
from core.Halt import Halt
from parse import Parser
from core.World import World
from app import app, update_screen_loop
from core.DocileThread import DocileThread


if __name__ == '__main__':

    parser = Parser()
    world = World()

    try:
        path_script = os.path.abspath(sys.argv[1])
        world.set_path_script(path_script)
        text = open(path_script, 'r').read()
        ast = parser.parse(text)
        assert isinstance(ast, Ast)
        res = ast.execute(world)
        if isinstance(res, Halt):
            exit()

        app.config['world'] = world
        game_loop_thread = DocileThread(world.game_loop, [])
        server_thread = DocileThread(lambda: app.run(host='0.0.0.0', port=8000), [])
        update_screen_thread = DocileThread(update_screen_loop, [world])

        game_loop_thread.start()
        server_thread.start()
        update_screen_thread.start()

        game_loop_thread.join()
        server_thread.join()
        update_screen_thread.join()

    except Halt as e:

        print(e.full_message)
        exit(e.is_error)

    except Exception as e:

        raise e
