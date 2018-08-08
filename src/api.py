import flask
from person import Person
import names
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
  personList = []
  for i in range(0, 5):
    personList.append(Person(names.get_first_name(), names.get_last_name()))
    jsonStr = json.dumps([p.toJSON() for p in personList ])

  return jsonStr

app.run()