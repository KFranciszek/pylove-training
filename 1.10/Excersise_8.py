# Klasa Prostopadłościan jest klasą nadrzędną dla klas Sześcian i Walec,
# a klasa Stożek dziedziczy z klasy Walec

from math import pi


class Prostopadloscian:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h


    def objetosc(self):
        return self.a * self.b * self.h


class Szescian(Prostopadloscian):
    def __init__(self, a):
        super().__init__(a, a, a)


class Walec(Prostopadloscian):
    def __init__(self, r, h):
        super().__init__(r, r, h)


    def objetosc(self):
        return pi * super().objetosc()


class Stozek(Walec):
    def objetosc(self):
        return 1/3 * super().objetosc()


success = False
wybor = 0
print("Kalkulator objętości brył!")
print("Wybierz bryłę: 1 - prostopadłościan, 2 - sześcian, 3 - walec, 4 - stożek.")
while not success:
    try:
        wybor = int(input("Podaj numer bryły: "))
        if wybor - 1 in range(0, 4):
            success = True
        else:
            print("Nie znam tej bryły!")
    except ValueError:
        print("Podaj liczbę!")
success = False
if wybor == 1:
    szer = 0
    gleb = 0
    wys = 0
    while not success:
        try:
            szer = float(input("Podaj długość jednego boku podstawy w cm: "))
            success = True
        except ValueError:
            print("Podaj wartość liczbową.")
    success = False
    while not success:
        try:
            gleb = float(input("Podaj dlugość drugiego boku podstawy w cm: "))
            success = True
        except ValueError:
            print("Podaj wartość liczbową.")
    success = False
    while not success:
        try:
            wys = float(input("Podaj wysokość prostopadłościanu w cm: "))
            success = True
        except ValueError:
            print("Podaj wartość liczbową.")
    print("Objętość prostopadłościanu wynosi {} cm3.".format(Prostopadloscian(szer, gleb, wys).objetosc()))
elif wybor == 2:
    bok = 0
    while not success:
        try:
            bok = float(input("Podaj długość boku sześcianu w cm: "))
            success = True
        except ValueError:
            print("Podaj wartość liczbową.")
    print("Objętość sześcianu wynosi {} cm3.".format(Szescian(bok).objetosc()))
else:
    promien = 0
    wys = 0
    while not success:
        try:
            promien = float(input("Podaj długość promienia podstawy w cm: "))
            success = True
        except ValueError:
            print("Podaj wartość liczbową.")
    success = False
    while not success:
        try:
            wys = float(input("Podaj wysokość bryły w cm: "))
            success = True
        except ValueError:
            print("Podaj wartość liczbową.")
    if wybor == 3:
        print("Objętość walca wynosi {} cm3.".format(Walec(promien, wys).objetosc()))
    else:
        print("Objętość stożka wynosi {} cm3.".format(Stozek(promien, wys).objetosc()))
