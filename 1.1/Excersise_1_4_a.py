def cenzura_cyfr(tekst):
    for i in range(10):
        tekst = tekst.replace(str(i),"#")
    return tekst


print(cenzura_cyfr("pass4125896"))
print(cenzura_cyfr("pass"))
print(cenzura_cyfr("A1a ma k0ta"))