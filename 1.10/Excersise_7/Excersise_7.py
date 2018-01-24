from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("google.html")

@app.route("/search", methods=['GET', 'POST'])
def szukaj():
    return redirect("http://thecatapi.com/api/images/get")


app.run(debug=True)