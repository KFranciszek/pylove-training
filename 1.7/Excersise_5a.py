from flask import Flask, request
import json

app = Flask(__name__)
users = []
@app.route("/")
def hello():
    return str(users)

@app.route("/users/add", methods=["POST"])
def add_user():
    data = request.get_json() #  {"imie": "Grzegorz", "wiek": "26", "plec": "m"}
    users.append(data)
    return "User successfully added to the database. {}".format(str(users))

@app.route("/users/stats", methods=["GET"])
def get_stats():
    stats = {
        "ilosc osob": len(users),
        "kobiety": 0,
        "mezczyzni": 0,
        "średni wiek" : 0,
        "najpopularniejsze imie": '',
    }
    wiek_suma = 0
    imiona = []
    # max_name = users[0]['imie']
    for user in users:
        wiek_suma += int(user['wiek'])
        imiona.append(user['imie'])
        if user['plec'] == 'k':
            stats["kobiety"] += 1
        else:
            stats["mezczyzni"] += 1
    stats["średni wiek"] = wiek_suma / stats["ilosc osob"]
    return str(stats)

app.run(debug=True)