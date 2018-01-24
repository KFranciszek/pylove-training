from flask import Flask, request, redirect, render_template

app = Flask(__name__)

zadania = []

@app.route("/zadania", methods=['GET', 'POST'])
def lista_zadan():
    if request.method == 'POST':
        zadania.append(request.form['zadanie'])
        return redirect('/zadania')

    return render_template('zadania.html', zadania=zadania)

app.run(debug=True)