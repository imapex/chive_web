from flask import Flask
from flask import render_template
import requests


app = Flask(__name__)


@app.route('/')
@app.route('/info')
def index():
    url = "http://127.0.0.1/device"

    headers = {'cache-control': "no-cache"}

    try:
        devices = requests.get("GET", url, headers=headers)
        return render_template('device_info.html',
                               title='CHIVE : Cisco Heat Indication & Visualization Engine', devices=devices)

    except:
        print "Problem posting...trying again..."
        pass


# !flask/bin/python
app.run(debug=True)

