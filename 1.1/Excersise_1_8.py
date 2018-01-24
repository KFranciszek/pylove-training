#Napisz funkcję, która policzy drogę pokonaną przez samochód w czasie t i przyspieszeniu a z opcjonalną prędkością początkową,
#domyślnie równą 0. >>> droga(5, 5) 62.5 >>> droga(10, 10, vs=100) 1500

def droga(t, a, vs = 0):
    return vs * t + a * t * t / 2

print(droga(5, 5))
print(droga(10, 10, vs=100))