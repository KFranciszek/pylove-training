from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

users = {
    "user1" : {"password" : "password1"},
    "user2" : {"password" : "password2"}
}

@app.route("/user/<username>/set-password", methods=["POST"])
def setpass(username):
    data = request.get_json() # {"password" : "new password"}
    users[username] = {"password": data["password"]}
    return "Password was successfully changed!"

@app.route("/users", methods=["GET"])
def get_users():
    return str(users)

@app.route("/user/<username>/login", methods=["GET"])
def login(username):
    data = request.get_json()  # {"password" : "users_password"}
    if users[username]["password"] == data["password"]:
        return "Login successful"
    else:
        return "Wrong password"

app.run(debug=True)