# char() ord() >>> ord("a") 97 >>> chr(98) "b" f
# zaimplementuj szyfr cezara, który jako drugi parametr będzie brał przesunięcie.
# Przykłady szyfr cezaraz o parametrze 3 podmieni każd literka alfabetu na trzecią z kolei np A na D a Z na C.
# >>> cezar("abc", 2) "cde" >>> cezar("abc", -2) "yza"
# Pamiętaj żeby znaki inne niż litery nie zmieniać. uwzględnij dodatkowo wielkie litery


def cezar(tekst, dif):
    tekst = list(tekst)
    while dif < 0:
        dif = dif + 26
    for i, let in enumerate(tekst):
        if ord(let) >= 65 and ord(let) <= 90:
            tekst[i] = chr((ord(let) - 65 + dif ) % 26 + 65)
        if ord(let) >= 97 and ord(let) <= 122:
            tekst[i] = chr((ord(let) - 97 + dif ) % 26 + 97)
    return "".join(tekst)


print(cezar("AAA ZZZ aaa zzz", 1))
print(cezar("AAA ZZZ aaa zzz", 3))
print(cezar("abc", 2))
print(cezar("abc", -2))
print(cezar("DDD CCC ddd ccc", -3))
