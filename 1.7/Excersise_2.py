from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

saved = "Initial data"
@app.route("/current_status", methods=["POST"])
def save():
    global saved
    data = request.get_json()   # {"status":"new status"}
    saved = data["status"]
    return "Current status {}".format(data["status"])
@app.route("/current_status", methods=["GET"])
def read():
    return saved
app.run(debug=True)
