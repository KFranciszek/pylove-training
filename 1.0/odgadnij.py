# wyświetla informację ile gier rozegrano, ile wygrano, ile przegrano.

import random
game = "y"
games = 0
won = 0
lost = 0
while game == "y":
    rounds = 1
    games += 1
    print("Zagrajmy w grę! Odgadnij liczbę, którą mam na myśli.")
    print("Wybierz tryb gry. Wpisz 1 jeżeli chcesz w pięciu rundach odgadnąć liczbę z przedziału od 0 do 100. ")
    print("Wpisz 2 jeżeli chcesz w siedmiu rundach odganąć liczbę z przedziału od 0 do 1000.")
    mode = 0
    while mode != 1 and mode != 2:
        try:
            mode = int(input("Wybierz tryb: "))
            if mode != 1 and mode != 2:
                raise ValueError
        except ValueError:
            print("Podaj 1 lub 2.")
    if mode == 1:
        rounds_max = 5
    else:
        rounds_max = 7
    print("Wybrano tryb: {0}, masz {1} szans.".format(mode, rounds_max))
    if mode == 1:
        rand_number = random.randint(0, 100)
    else:
        rand_number = random.randint(0, 1000)
    while rounds <= rounds_max:
        try:
            user_number = int(input("Zgadnij jaką liczbę mam na myśli: "))
            if user_number == rand_number:
                print("Brawo! To jest właśnie szukana liczba, zgadłeś ją w {} krokach.".format(rounds))
                rounds = 10
            elif user_number > rand_number:
                print("Moja liczba jest mniejsza.")
            else:
                print("Moja liczba jest większa.")
            rounds += 1
        except ValueError:
            print("Podaj liczbę!")
    if rounds == rounds_max + 1:
        print("Koniec szans. Niestety przegrałeś.")
        lost += 1
    else:
        print("Jesteś zwycięzcą!")
        won += 1
    game = input("Gramy jeszcze raz? y/n ")
    if game != "y":
        print("Rozegrano {0} gier, {1} ({2}%) wygrano, a {3} ({4}%) przegrano.".format(games, won, round(100*won/(won+lost), 2), lost, round(100*lost/(won+lost), 2)))
