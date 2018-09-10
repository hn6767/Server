from flask import Flask
from game import exput
app = Flask(__name__)

@app.route('/index')
def hello():
  str = "Hello there"
  return str


@app.route('/game/<name>')
def main1(name):
  return exput(name)
  