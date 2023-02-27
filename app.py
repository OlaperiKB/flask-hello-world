from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/redeploy')
def hello_world():
    return 'Just testing an update'