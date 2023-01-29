import flask
from flask import request



app = flask.Flask('DAVEs')

@app.route('/')
def home_dir():
    return 'hello world'

def retinsults(sent):
    


@app.route('/analysis',methods=['POST'])
def analysis():
    rev_json = request.get_json()
    print(rev_json)
    sentence = rev_json['sentence']




app.run('0.0.0.0',8080)