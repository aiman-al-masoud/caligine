import os
from flask import Flask, request

from core.World import KeyEvent

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    path_index = os.path.split(os.path.abspath(__file__))[0]+'/frontend/index.html'
    return open(path_index).read()

@app.route('/api/input', methods=['GET', 'POST'])
def get_input():

    if not request.json: return 'missing json', 400    
    e = KeyEvent(request.json['client_id'], request.json['key'], request.json['state'])
    app.config['world'].put_event(e)

    return 'ok'

