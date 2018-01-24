def cenzura_cyfr(tekst):
    tekst = list(tekst)
    for inx, let in enumerate(tekst):
        try:
            int(let)
            tekst[inx] = "#"
        except ValueError:
            pass
    return "".join(tekst)


print(cenzura_cyfr("pass1253622"))
print(cenzura_cyfr("A1a ma k0ta"))
