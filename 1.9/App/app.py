from flask import Flask, request, redirect, render_template

app = Flask(__name__)

stan_konta = 1000
przelewy = []
blad = False
@app.route("/")
def index():
    return redirect("/konto")

@app.route("/konto", methods=['GET', 'POST'])
def wyslij_przelew():
    global stan_konta
    if request.method == 'POST':
        kwota = int(request.form.get('kwota'))
        nr_konta = request.form.get('nr_konta')
        stan_konta -= kwota
        przelewy.append({'kwota': kwota,'nr_konta': nr_konta})
        return redirect('/konto')

    return render_template('index.html', stan_konta = stan_konta, przelewy = przelewy)

app.run(debug=True)