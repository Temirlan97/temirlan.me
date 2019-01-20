import os
from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from flask import send_from_directory
from flask import url_for
from myutils import log
from myutils.sendEmail import notifyViaEmail
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('DevFolio/index.html')

@app.route('/message', methods=['POST'])
def message():
   try:
      name = request.values.get('name')
      email = request.values.get('email')
      subject = request.values.get('subject')
      message = request.values.get('message')
      body = "Sender: " + name + "\n\n"
      body += "Sender's email: " + email + "\n\n"
      body += "Subject: " + subject + "\n\n"
      body += "Message:\n" + message + "\n\n"
      notifyViaEmail("ulugbekuulutemirlan@gmail.com", "Letter from visitor(" + name + ") of temirlan.me", body)
      return 'OK'
   except Exception as e:
      log.errorLog(e)
      return "Ooooops, something went wrong. I will soon find out and hunt down the bug! <br /> Meanwhile feel free to send email manually using contact details on the right."

@app.route('/bsc-thesis')
def bsc_thesis():
   return send_file('static/other/bsc-2018-thesis.pdf')

if __name__ == '__main__':
   # context = ('temirlan_me.crt', 'temirlan_me.key')
   # app.run(host='0.0.0.0',port='5000',ssl_context=context,debug=True)
   app.run(host='0.0.0.0',port='5000',debug=True)