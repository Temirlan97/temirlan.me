from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('DevFolio/index.html')

@app.route('/pg')
def pg():
   return render_template('DevFolio/index.html')


if __name__ == '__main__':
   app.run(host='0.0.0.0', port='5000',debug = True)