from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/hello")
def hello_name():
    name = request.args.get("name", "")
    return render_template(
        'index.html',
        name =  name
    )

app.run(debug=True)