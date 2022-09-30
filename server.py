import io
from flask import Flask
from flask import send_file
from flask import request

import json, requests

from src import core, props
from props import bcolors

app = Flask(__name__)

# address to the api 
# there is one entry file - json with options considering the song to be exported
#                           and text of the song - both in one json file
@app.route('/data_to_file_export', methods=['GET', 'POST'])
def data_to_file_export():
    json_content = json.loads(request.get_json()) # TODO content redy to read

    fileName = core.exportJsonToFile(json_content)
    
    return send_file(fileName, as_attachment=True)

@app.route('/') #TODO make it nice
def home():
    return "Welcome to the home site"

@app.route('/doc') #TODO write doc
def doc():
    try:
        return send_file('/doc/readme.pdf', as_attachment=True)
    except Exception  as e:
        print(str(e))

