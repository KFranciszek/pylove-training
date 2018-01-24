print('{0} {1} {2}, \n {3} przyjacielu chciałbym Cię zaprosić na swoje urodziny, na których będę serwował Twój ulubiony {4} tort. \n Piotr'.format('Prof.','Andrzej','Ruda','Najbliższy','kokosowy'))

dane = ('Prof.', 'Andrzej', 'Ruda', 'Najbliższy','kokosowy')
print('{0} {1} {2}, \n {3} przyjacielu chciałbym Cię zaprosić na swoje urodziny, na których będę serwował Twój ulubiony {4} tort. \n Piotr'.format(*dane))

dane2 = {'tytul': 'Prof.', 'imie': 'Andrzej', 'nazwisko': 'Ruda', 'przymiotnik': 'Najbliższy', 'smak':'kokosowy'}
print('{tytul} {imie} {nazwisko}, \n {przymiotnik} przyjacielu chciałbym Cię zaprosić na swoje urodziny, na których będę serwował Twój ulubiony {smak} tort. \n Piotr'.format(**dane2))