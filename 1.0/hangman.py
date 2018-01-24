import random
words = ["poliglota",
         "pieczarka",
         "traktor",
         "kaloryfer",
         "krokodyl",
         "komputer",
         "monitor",
         "bateria",
         "lekarz",
         "autobus",
         "orangutan",
         "semafor",
         "bulterier",
         "patison",
         "czerpak",
         "galaretka",
         "porcelana",
         "pokrowiec",
         "zajezdnia",
         "wyciskarka",
         "imponderabilia"]
print("Spróbuj w pieciu krokach odgadnąć wyraz, który mam na myśli. Wyrazy są w języku polskim. Kategoria: \
COKOLWIEK. Każda próba się liczy, więc rozsądnie dobieraj litery i słowa. Wielkość liter nie ma znaczenia :-)")
rounds = 1
current_word = words[random.randint(0, len(words)-1)]
current_word_list = list(current_word)
user_word_list = list("*"*len(current_word))
print("Wybrałam dla Ciebie słowo: " + "".join(user_word_list))
while rounds <= 5:
    user_letter = input("Runda {} - Podaj literę lub odgadnij słowo: ".format(rounds)).lower()
    if len(user_letter) > 1:
        if user_letter == current_word:
            print ("Brawo! Odgadłeś wyraz {0} w {1} próbach.".format(current_word, rounds))
            rounds = 10
        else:
            print ("To nie jest szukany wyraz, spróbuj jeszcze raz...")
            print ("".join(user_word_list))
            rounds += 1
    else:
        if user_letter in current_word_list:
            print("Brawo, zgadłeś literę!")
            for i, let in enumerate(current_word_list):
                if let == user_letter:
                    user_word_list[i] = user_letter
        else:
            print("Spróbuj jeszcze raz!")
        print("".join(user_word_list))
        rounds += 1
if rounds == 10:
    print("Wygrałeś!")
else:
    print("Koniec szans! Przegrałeś!")