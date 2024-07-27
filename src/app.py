import os
import sys
from flask import Flask
from core.KeyEvent import KeyEvent
from flask import Flask
from flask_socketio import SocketIO
import logging


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
    return open(path_index, 'r').read()

@socketio.on('client-connected')
def handle_client_connected(data):

    client_id = data['client_id']
    print('client connected!', client_id)
    app.config['world'].on_client_connected(client_id)

@socketio.on('keyevent')
def handle_keyevent(data):

    e = KeyEvent(client_id=data['client_id'], key=clean_key_name(data['key']), state=data['state'])
    app.config['world'].put_event(e)

def clean_key_name(key_name:str):
    
    if key_name == ' ':
        return 'Space'
    else:
        return key_name
