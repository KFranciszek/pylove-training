def xo_checker(tekst):
    xos = list(tekst)
    x_count = 0
    o_count = 0
    for let in xos:
        if let != "x" and let != "o":
            return "Illegal letters in text"
        if let == "x":
            x_count += 1
        else:
            o_count += 1
    return x_count == o_count


print(xo_checker("xxooodddxoooo"))
print(xo_checker("xxoooxoooo"))
print(xo_checker("xxoo"))