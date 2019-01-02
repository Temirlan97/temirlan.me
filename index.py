import os
from flask import Flask
from flask import render_template
from flask import url_for
from flask import send_from_directory
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('DevFolio/index.html')

@app.route('/message', methods=['POST'])
def message():
   return render_template('DevFolio/message.html')

if __name__ == '__main__':
   # context = ('temirlan_me.crt', 'temirlan_me.key')
   # app.run(host='0.0.0.0',port='5000',ssl_context=context,debug=True)
   app.run(host='0.0.0.0',port='5000',debug=True)