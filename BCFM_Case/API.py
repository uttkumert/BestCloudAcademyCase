
import requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

names = {"firstname": "utku", "lastname": "mert"}

@app.route("/whoami")
def x1():
    return jsonify(names)

@app.route("/alert")
def x2():
    url = 'https://webhook.site/26ea7387-4afc-4c0b-ace9-3e429f161b8a'
    r = requests.post('https://webhook.site/26ea7387-4afc-4c0b-ace9-3e429f161b8a', data = names)
    return r.text
    
    
