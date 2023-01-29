import flask
from flask_cors import CORS




app = flask.Flask(__name__)
CORS(app)
@app.route('/data',methods=['POST'])
def data():
    return {}
@app.route('/')
def re():
    return ['wetwe','wetwet']
app.run('0.0.0.0',8080)