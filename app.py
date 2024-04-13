from flask import Flask, jsonify, request

import json

with open('db.json') as file:
    data = json.load(file)

def getCities(state):
    cities = data[state].values()
    return list(cities)[0].values()

def getAllStates():
    states = list(data.keys())
    return states

app = Flask(__name__)

@app.route("/allStates", methods=["POST", "GET"])
def all():
    return jsonify(getAllStates())

@app.route("/states/<state>", methods=["POST", "GET"])
def stateRoute(state):
    s = list(getCities(state))
    return jsonify(s)

if __name__ == "__main__":
    app.run(debug=True)