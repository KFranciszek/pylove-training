""" Whatever """
# Napisz prosty konwerter walut, który na wejściu przyjmie stringa składającego się z:
# kwoty, waluty wejściowej, słówka kluczowego "to" i kwoty wyjściowej.
# Użyj następujących kursów: 1 PLN to 1000 USD, 1 PLN to 4505 EURO, 1 PLN to 100 JPY
# Załóż, że konwersje są wykonywane tylko z lub do PLNów.
# Dla zaawansowanych: przeliczaj wszystkie waluty między sobą (PLN, USD, EURO, JPY)
# Przykład:
# input: "2 PLN to USD" output: "2000 USD"
# input "15 USD to PLN" output: "0.015 PLN"

import re
def konwerter(request):
    """ FUnkcja konwertująca waluty """
    kurs = {
        'pln' : {
            'pln': 1,
            'usd': 1000,
            'eur': 4505,
            'jpy': 100,
        },
        'usd': {
            'pln': 0.001,
            'usd': 1,
            'eur': 4.505,
            'jpy': 0.1,
        },
        'eur': {
            'pln': 1 / 4505,
            'usd': 1 / 4.505,
            'eur': 1,
            'jpy': 100 / 4505,
        },
        'jpy': {
            'pln': 0.01,
            'eur': 45.05,
            'usd': 10,
            'jpy': 1
        }
    }
    request = request.split(' ')
    try:
        response = '{0} {1}'.format(
            int(request[0]) * kurs[request[1].lower()][request[3].lower()],
            request[3],
        )
    except KeyError:
        return "Brak w bazie danych kursu dla podanych walut"
    return response


valid = False
query = ''
print("Podaj, jakiej konwersji walut chciałbyś dokonać.")
while not valid:
    query = input('Oczekiwany format "<kwota> <symbol waluty> to <symbol waluty>"')
    pattern = '[0-9]* [A-Z]{3,3} to [A-Z]{3,3}'
    if re.match(pattern, query):
        valid = True
print('Poprawny format danych.')
print(konwerter(query))
