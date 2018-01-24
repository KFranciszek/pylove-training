from pprint import pprint as pp
zliczacz = {}
wyraz = input('Podaj tekst: ')

for let in wyraz:
    if let in zliczacz:
        zliczacz[let] += 1
    else:
        zliczacz[let] = 1
    print(zliczacz)

pp(zliczacz)