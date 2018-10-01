from flask import Flask, request
import names
import json
import cv2
import numpy as np

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/analyze', methods=['POST'])
def analyze():
  r = request
  print(r)
  nparr = np.fromstring(r.data, np.uint8)
  # decode image
  img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
  print(img)
  return "show"

app.run()