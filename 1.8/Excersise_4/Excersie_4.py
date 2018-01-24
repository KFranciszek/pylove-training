# Utwórz klasę Osoba. Każda instancja tej klasy powinna posiadać trzy atrybuty – imię, nazwisko i wiek.
# Utwórz listę kilku dowolnych osób. Utwórz szablon HTML, który będzie renderował tabelę osób
# (imię, nazwisko i wiek powinny wyświetlać się w osobnych kolumnach).
# Napisz program, który po wejściu na adres /osoby renderuje ten szablon. Przetestuj program w przeglądarce.

from flask import Flask, render_template

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

app = Flask(__name__)
persons = [
    Person("Anna", "Nowak", 24),
    Person("Tomasz", "Kowalski", 56),
    Person("Zofia", "Makowska", 31),
    Person("Alicja", "Wonder", 13)
]

@app.route("/")
def tabelka():
    return render_template(
        'index.html',
        naglowek='Lista osób',
        persons= persons,
    )

app.run(debug=True)
