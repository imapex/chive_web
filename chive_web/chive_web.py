# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
import requests
import json
import os

chive_app = os.environ['CHIVE_APP']

app = Flask(__name__)


@app.route('/')
@app.route('/info')
def index():

    url = 'http://' + chive_app + '/device'
    headers = {"Content-Type": "application/json"}

    try:
        # make request to GET data from REST API
        response = requests.get(url=url, headers=headers)
        # put the data in JSON format
        devices = json.loads(response.text)
        # render data to webpage
        return render_template('index.html',
                           title='CHIVE : Cisco Heat Indication & Visualization Engine', devices=devices)

    except:
        print "Problem getting data...trying again..."
        pass


app.run(debug=False, host='0.0.0.0', port=8080)
