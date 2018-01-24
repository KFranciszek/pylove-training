from flask import Flask, request, render_template, redirect

app = Flask(__name__)
users = {}
message = ""

@app.route("/", methods=["GET"])
def index():
    return redirect("/users")


@app.route("/users", methods=["GET", "POST"])
def add_user():
    global message
    if request.method == "POST":
        name = request.form["name"]
        if name in users:
            message = "Użytkownik o podanej nazwie jest już zarejestrowany."
        else:
            users[name] = request.form["pass"]
            message = "Użytkownik dodany do bazy"
        return redirect("/users")
    return render_template("add_user_form.html", message=message)


app.run(debug=True)