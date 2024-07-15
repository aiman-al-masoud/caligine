import os
import sys
from threading import Thread
from flask import Flask, json
from core.Client import Client
from core.KeyEvent import KeyEvent
from flask import Flask
from flask_socketio import SocketIO
from time import sleep
import logging
from core.World import World


app = Flask(__name__)
app.config['SECRET_KEY'] = 'buruf'
socketio = SocketIO(app)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None # pyright:ignore

@app.route('/', methods=['GET'])
def index():

    path_index = os.path.split(os.path.abspath(__file__))[0]+'/frontend/index.html'
    return open(path_index).read()

@socketio.on('client-connected')
def handle_message(data):

    client_id = data['client_id']
    print('client connected!', client_id)
    send_updated_sprites(client_id, include_image=True)

@socketio.on('keyevent')
def handle_keyevent(data):

    e = KeyEvent(client_id=data['client_id'], key=data['key'], state=data['state'])
    app.config['world'].put_event(e)

def update_screen_loop(world:World):

    while True:

        clients=  [x for x in world.values() if isinstance(x, Client)]
        for client in clients:
            send_updated_sprites(client.get_name(), include_image=False)

        sleep(0.1)

def start_update_screen(world:World):

    Thread(target=update_screen_loop, args=[world]).start()

def send_updated_sprites(client_id:str, include_image:bool=False):

    world = app.config['world']
    assert isinstance(world, World)
    client = world.get(client_id)
    assert isinstance(client, Client)

    if not client:
        socketio.emit('error', json.dumps({'error':f'Client {client_id} (you) does not exist.'}))
        return

    view = client.see_world(world, include_image)
    socketio.emit('update-sprites', json.dumps(view))
