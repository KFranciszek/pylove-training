from flask import Flask, redirect
app = Flask(__name__)
@app.route("/hello")
def hello():
    return 'Hello World!'

@app.route("/witam")
def witam():
    return redirect('/hello')

app.run(debug=True)