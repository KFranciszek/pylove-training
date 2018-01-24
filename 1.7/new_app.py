from flask import Flask, request

app = Flask(__name__) # objekt aplikacja

@app.route("/hello")     # dekorator, który przekazuje ścieżkę, pod którą ma być widoczna aplikacja
def hello():
    return "Hello World!"
@app.route("/hello/<name>") # do podawania parametrów
def welcome(name):
    return "Welcome {}!".format(name)
# metoda POST
saved = "Data"
@app.route("/save", methods=["POST"])
def save():
    global saved    # odwołanie do zmiennej globalnej saved
    data = request.get_json()   # json zawierający zapytanie użytkownika np. {"value":"dowolny tekst"}
    saved = data["value"]   # odczytuję wartość value i zapisuje w zmiennej saved
    return "Saved {}".format(data["value"]) # zwraca informację dla użytkownika
@app.route("/read", methods=["GET"])    # domyślną metodą jest GET
def read():
    return saved    # zwraca wartość z serwera
app.run(debug=True)
