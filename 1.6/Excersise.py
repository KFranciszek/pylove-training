class Czas:
    def __init__(self, godz=0, minut=0, sek=0):    # inicjalizaja z domyślnymi wartościami => argumenty opcjonalne
        self.godz = godz
        self.minut = minut
        self.sek = sek

# funkcja magiczna__str__ pozwoli printować atrybuty obiektu zamiast wyświetlania obiektu i jego adresu w pamięci
# w tej postaci może być dziedziczona i jest uniwersalna dla wszystkich podklas
    def __str__(self):
        temp =  '{} '.format(self._get_name())    # na początku strona jest nazwa klasy zwracana przez funkcję klasową _get_name
        for atr in vars(self):  # vars zwraca argumenty, pomija metody
            temp += '{}={} '.format(atr, getattr(self, atr))    # atr daje nazwę parametru a funkcja getattr zwraca jego wartość
        return temp
# jeżeli korzysta się w pętli z dir(self) trzeba skorzystać z instrukcji if not atr.startswith('_'): eliminującej
    # metody magiczne i prywatne oraz innych warunków eliminujących własne napisane metody tej klasy

    @classmethod
    def _get_name(cls):
        return cls.__name__

    def set_time(self, godz=None, minut=None, sek=None):
        if godz:
            self.godz = godz
        if minut:
            self.minut = minut
        if sek:
            self.sek = sek
    # inna opcja zamiast powyższych if'ów
    #     self.godz = godz or self.godz
    #     self.minut = minut or self.minut
    #     self.sek = sek or self.sek

    def add_time(self, godz=0, minut=0, sek=0):
        self.godz += godz
        self.minut += minut
        self.sek += sek
        if self.sek >= 60:    # jeżeli przekraczamy 60 sekund
            self.minut += self.sek // 60    # dodajemy wynik dzielenia całkowitego do minut
            self.sek = self.sek % 60    # ustawiamy sekundy na resztę z modulo
        if self.minut >= 60:    # analogicznie do sekund
            self.godz += self.minut // 60
            self.minut = self.minut % 60

    def get_seconds(self):
        return self.godz * 3600 + self.minut * 60 + self.sek

    def get_minutes(self):
        return self.get_seconds() / 60

    def get_hours(self):
        return self.get_seconds() / 3600


class Zegar(Czas):
    def __init__(self, format_cz, **kwargs):
        super().__init__(**kwargs)
        self.format_cz = format_cz


class DokladnyZegar(Zegar):
    def __init__(self, *args, milisek=0, **kwargs):
        super().__init__(*args, **kwargs)
        self.milisek = milisek

    def set_time(self, milisek=None, **kwargs):
        super().set_time(**kwargs)
        if milisek:
            self.milisek = milisek


def mojprint(tresc, ile, prefix=''):
    for i in range(ile):
        print('{}{}'.format(prefix, tresc))


moj_czas = Czas()
moj_czas_2 = Czas(17, 23, 0)
print(moj_czas)
print(moj_czas_2)
moj_zegar = Zegar('12H')
print(moj_zegar)
moj_dokl_zegar = DokladnyZegar('24H', godz=15, minut=20, sek=30, milisek=0)
print(moj_dokl_zegar)
moj_czas.set_time(godz=8, minut=0, sek=7)
print(moj_czas)
moj_dokl_zegar.set_time(godz=3, milisek=15)
print(moj_dokl_zegar)
mojprint(moj_zegar, 2)
moj_czas.add_time(godz=1, minut=150, sek=170)
print(moj_czas)
print(moj_czas.get_seconds())
print(moj_czas.get_minutes())
print(moj_czas.get_hours())
