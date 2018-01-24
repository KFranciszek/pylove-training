def policz_samogloski(tekst):
    samogloski = ["a", "e", "ą", "ę", "i", "y", "u", "o", "ó"]
    licznik = 0
    litery = list(tekst.lower())
    for let in litery:
        if let in samogloski:
            licznik += 1
    return licznik


print(policz_samogloski('Ala ma kota'))
print(policz_samogloski('Pies psu niedzwiedziem'))
