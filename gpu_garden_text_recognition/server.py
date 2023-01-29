import flask
from flask_cors import CORS
from flask import request
from transformers import AutoModelForSequenceClassification, AutoTokenizer, TextClassificationPipeline
model = AutoModelForSequenceClassification.from_pretrained("unitary/toxic-bert",problem_type="multi_label_classification")
tokenizer = AutoTokenizer.from_pretrained("unitary/toxic-bert")
import smtplib, ssl
from email.message import EmailMessage
port = 465  # For SSL
import threading
import random
import time
import json

app = flask.Flask('DAVEs')
CORS(app)
@app.route('/')
def home_dir():
    return 'hello world'    

def proc_sentence(sentence):
    pipeline = TextClassificationPipeline(model=model, tokenizer=tokenizer, device=0)
    prediction = pipeline(sentence, top_k=10)
    return prediction



def send_notification(labels):
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("mail.riseup.net", port, context=context) as server:
            server.login('poghacking7@riseup.net', '_Bananapopcorn2_')
            msg = EmailMessage()
            msg['Subject'] = 'DAVES Child report'
            msg.set_content(labels)
            msg["From"] = 'poghacking7@riseup.net'
            msg["To"] = 'amy2008chang@gmail.com'
            e = server.send_message(msg)
            server.quit()
            return True
    except Exception as e:
        print(e)

@app.route('/notify',methods=['POST'])
def notif():
    rev_json = request.get_json()
    #{'message':['toxic', 'identity_hate', 'insult', 'obscene']}
    labez = rev_json['message']
    if send_notification(labez):
        return {'status' : 'success'}

@app.route('/analysis',methods=['POST'])
def analysis():
    rev_json = request.get_json()
    print(rev_json)
    sentence = rev_json['sentence']
    preds = proc_sentence(sentence)
    labels = []
    for label in preds:
        if (label['score'] >= .35):
            labels.append(label['label'])
    print(labels)
    return {'labels' : labels}
    



app.run('0.0.0.0',8080,ssl_context='adhoc')