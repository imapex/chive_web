# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
import requests
import json
import os

chive_app_ip = os.environ('APP_PORT_5000_TCP_ADDR')
app = Flask(__name__)


@app.route('/')
@app.route('/info')
def index():

    url = 'http://' + chive_app_ip + ':5000/device'

    headers = {"Content-Type": "application/json"}

    try:
        # make request to GET data from REST API
        response = requests.get(url=url, headers=headers)
        # put the data in JSON format
        devices = json.loads(response.text)
        # render data to webpage
        return render_template('device_info.html',
                               title='CHIVE : Cisco Heat Indication & Visualization Engine', devices=devices)

    except:
        print "Problem getting data...trying again..."
        pass


app.run(debug=True, host='0.0.0.0', port=8080)
