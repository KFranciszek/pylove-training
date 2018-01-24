from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/planet-details", methods=["GET"])
def get_planet_details():
    planet = request.args.get("planet", "")
    resp = requests.get("https://swapi.co/api/planets/?search={}".format(planet)).json()["results"]
    if len(resp) == 0:
        return "Planet {} does not exist.".format(planet)
    else:
        return str(resp[0])


app.run(debug=True)
