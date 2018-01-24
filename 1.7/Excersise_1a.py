from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/add/<int:liczba1>/<int:liczba2>")
def sum(liczba1, liczba2):
    return "Suma wynosi {}".format(liczba1 + liczba2)

app.run(debug=True)