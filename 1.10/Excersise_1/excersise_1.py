#     title: 1. Proste wczytywanie plików
#     task: |
#         Napisz program, który w zależności od opcji podanej przez użytkownika (1, 2 lub 3)
#         odczyta odpowiednio plik x.txt, y.txt lub z.txt (zawartość dowolna);
#         obsługa błędów powinna obejmować (co najmniej) komunikat o nieprawidłowej opcji,
#         zaś wczytywanie treści pliku powinno znaleźć się w oddzielnej funkcji (wraz z obsługą błędów)

def wczytaj_plik(adres):
    """ funkcja do wczytywania pliku """
    with open(adres, "r") as file:
        dane = file.read()
    return dane

invalid = True
adres = ''
while invalid:
    user_choice = input('Wprowadź który plik chcesz wczytać, podaj opcję 1, 2 lub 3 [1 - x.txt, 2 - y.txt, 3 - z.txt]')
    if user_choice == '1' or user_choice == '2' or user_choice == '3':
        invalid = False
    else:
        print('Podano niepoprawne dane, spróbuj jeszcze raz!')
    if user_choice == '1':
        adres = 'x.txt'
    elif user_choice == '2':
        adres = 'y.txt'
    else:
        adres = 'z.txt'
print(wczytaj_plik(adres))
