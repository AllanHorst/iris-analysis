from flask import Flask, request
from flask_cors import CORS, cross_origin
import names
import json
import cv2
import numpy as np
from process_image import process

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config["DEBUG"] = True

@app.route('/api/analyze', methods=['POST'])
@cross_origin(supports_credentials=True)
def analyze():
  r = request
  nparr = np.fromstring(r.data, np.uint8)
  img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
  process(img)
  return "show"

app.run()