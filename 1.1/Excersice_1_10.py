# czy liczba znaków "x" i "o" w stringu jest taka sama i zwróci True/False.
# Jeśli string zawiera coś innego niż "x" lub "o", to wypisze błąd.
#  >>> xo_checker("xoxoxoxoxoxo") True >>> xo_checker("xxxoooxxxxxxxo") False >>> xo_checker("xpd") "Illegal letters in text"


def xo_checker(tekst):
    for let in tekst:
        if let != "x" and let != "o":
            return "Illegal letters in text"
    if tekst.count("x") == tekst.count("o"):
        return True
    else:
        return False


print(xo_checker("xoxoxoxoxoxo"))
print(xo_checker("xpd"))
print(xo_checker("xxxoooxxxxxxxo"))
