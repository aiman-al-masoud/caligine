import os
from flask import Flask, json, request
from canvas import Canvas
from core.Client import Client
from core.KeyEvent import KeyEvent
from io import BytesIO
import base64

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    path_index = os.path.split(os.path.abspath(__file__))[0]+'/frontend/index.html'
    return open(path_index).read()

@app.route('/api/input', methods=['GET', 'POST'])
def get_input():

    payload = request.json
    if not payload: return 'missing json', 400    
    client_id = payload['client_id']
    key = payload['key']
    state = payload['state']
    e = KeyEvent(client_id, key, state)
    app.config['world'].put_event(e)
    return 'ok'

@app.route('/api/output', methods=['GET', 'POST'])
def send_output():

    payload = request.json
    if not payload: return 'missing json', 400    
    client_id = payload['client_id']
    client = app.config['world'].get_obj(client_id)
    assert isinstance(client, Client)
    canvas = Canvas(500, 500, 'white')
    client.look_at_world(app.config['world'], canvas)
    image = canvas.get_rendered()
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    out = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return json.dumps({
        'image_base64': 'data:image/png;base64,'+out
    })
