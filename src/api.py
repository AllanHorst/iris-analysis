import flask
import names
import json
import cv2

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():

  return ""

app.run()