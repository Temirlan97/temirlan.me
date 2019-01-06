import os
from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from flask import send_from_directory
from flask import url_for
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('DevFolio/index.html')

@app.route('/message', methods=['POST'])
def message():
   name = request.values.get('name')
   email = request.values.get('email')
   subject = request.values.get('subject')
   message = request.values.get('message')
   # TODO send the message here
   # return 'OK'
   return "I'm sorry, this functionality doesn't work yet, but I'm on it. <br /> Feel free to send email manually using contact details on the right."


@app.route('/bsc-thesis')
def bsc_thesis():
   return send_file('static/other/bsc-2018-thesis.pdf')

if __name__ == '__main__':
   # context = ('temirlan_me.crt', 'temirlan_me.key')
   # app.run(host='0.0.0.0',port='5000',ssl_context=context,debug=True)
   app.run(host='0.0.0.0',port='5000',debug=True)