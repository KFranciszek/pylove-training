from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/search", methods=['GET','POST'])
def search():
    query = request.form.get('query')
    return render_template(
        'index.html',
        query=query)

app.run(debug=True)
