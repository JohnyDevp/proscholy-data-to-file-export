from flask import Flask
from flask import send_file
from flask import request

app = Flask(__name__)

# address to the api 
# there is one entry file - json with options considering the song to be exported
#                           and text of the song - both in one json file
@app.route('/raw_data_export', methods=['GET', 'POST'])
def raw_data_export():
    ()

@app.route('/')
def home():
    ()

@app.route('/doc')
def doc():
    try:
        return send_file('/doc/readme.pdf', as_attachment=True)
    except Exception  as e:
        print(str(e))

