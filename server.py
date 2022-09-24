import io
from flask import Flask
from flask import send_file
from flask import request

import json, requests

from props import bcolors

app = Flask(__name__)

# address to the api 
# there is one entry file - json with options considering the song to be exported
#                           and text of the song - both in one json file
@app.route('/data_to_file_export', methods=['GET', 'POST'])
def data_to_file_export():
    print("Yes I have been raised")
    content = request.json
    return send_file("testpresent.odp", as_attachment=True)

@app.route('/')
def home():
    return send_file("testpresent.odp", as_attachment=True)

@app.route('/doc')
def doc():
    try:
        return send_file('/doc/readme.pdf', as_attachment=True)
    except Exception  as e:
        print(str(e))

