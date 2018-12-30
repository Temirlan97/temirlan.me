import os
from flask import Flask
from flask import render_template
from flask import url_for
from flask import send_from_directory
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('DevFolio/index.html')
   
@app.route('/.well-known/pki-validation/5ED2D1296FED2CC2A0EAEC6572EFA1A8.txt')
def ssl():
   return app.send_static_file('5ED2D1296FED2CC2A0EAEC6572EFA1A8.txt')


if __name__ == '__main__':
   app.run(host='0.0.0.0', port='5000',debug = True)