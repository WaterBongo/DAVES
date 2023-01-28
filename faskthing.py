import flask




app = flask.Flask('DAVEs')

@app.route('/')
def home_dir():
    return 'hello world'





app.run('0.0.0.0',8080)