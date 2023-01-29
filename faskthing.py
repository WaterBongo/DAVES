import flask
from flask import request



app = flask.Flask('DAVEs')

@app.route('/')
def home_dir():
    return 'hello world'    

@app.route('/analysis',methods=['POST'])
def analysis():
    rev_json = request.get_json()
    print(rev_json)
    sentence = rev_json['sentence']

    #PROCESS SENTANCE INTO LABELS LIST

    fakeData = [{'label': 'toxic', 'score': 0.9834303855895996}, {'label': 'obscene', 'score': 0.8534879684448242}, {'label': 'insult', 'score': 0.10630210489034653}, {'label': 'severe_toxic', 'score': 0.044429711997509}, {'label': 'threat', 'score': 0.005998513195663691}, {'label': 'identity_hate', 'score': 0.00374886323697865}]
    labels = []
    for label in fakeData:
        if (label['score'] >= .35):
            labels.append(label['label'])
    return {'labels' : labels}
    



app.run('0.0.0.0',8080)