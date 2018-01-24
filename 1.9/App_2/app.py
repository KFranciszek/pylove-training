from flask import Flask, redirect, request, render_template
import json
class Pracownik:
    def __init__(self, id, imie, nazwisko, placa, stanowisko):
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self.placa = placa
        self.stanowisko = stanowisko

pracownicy = [
    Pracownik(1, 'Anna', 'Nowak', 2563, 'księgowa'),
    Pracownik(2, 'Tomek', 'Kowalski', 5869, 'kierowca'),
    Pracownik(3, 'Marcin', 'Blady', 1258, 'magazynier'),
    Pracownik(4, 'Katarzyna', 'Orzechowska', 2365, 'asystentka zarządu'),
    Pracownik(5, 'Grzegorz', 'Rybczyński', 1999, 'whatever'),
    Pracownik(6, 'Paweł','Gaweł', 2569, 'who knows'),
]

app = Flask(__name__)

@app.route("/", methods=['GET'])
def przekierowanie():
    return redirect("/pracownicy")

@app.route("/pracownicy", methods=['GET', 'POST'])
def tabela():
    if request.method == 'POST':
        nowy_pracownik = Pracownik(
            int(request.form.get('id')),
            request.form.get('imie'),
            request.form.get('nazwisko'),
            int(request.form.get('placa')),
            request.form.get('stanowisko'))
        pracownicy.append(nowy_pracownik)
        return redirect('/pracownicy')
    return render_template('pracownicy.html', pracownicy=pracownicy)

@app.route("/pracownik/delete", methods=['GET', 'POST'])
def usun():
    if request.method == 'POST':
        id = int(request.args.get('id'))
        for i, prac in enumerate(pracownicy):
            if prac.id == id:
                pracownicy.pop(i)
        return redirect('/pracownicy')
    return render_template('pracownicy.html', pracownicy=pracownicy)

@app.route("/pracownik", methods=['GET'])
def pracownik_szczegoly():
    id = int(request.args.get('id'))
    pracownik = [prac for prac in pracownicy if prac.id == id][0]
    return render_template("/pracownik_szczegoly.html", pracownik=pracownik)



# @app.route("/pracownik/id=<int:id>", methods=['GET'])
# def pracownik_szczegoly(id):
#     pracownik = []
#     for prac in pracownicy:
#         if prac.id == id:
#             pracownik.append(prac)
#     pracownik = pracownik[0]
#     return render_template("/pracownik_szczegoly.html", pracownik=pracownik)

app.run(debug=True)