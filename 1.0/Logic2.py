def prostopad(a,b,c):
    volume = a*b*c
    if a==b:
        print('Twój prostopadłościan ma w podstawie kwadrat.')
        if b==c:
            print('Co wiecej, jest sześcianem foremnym!')
    print('Objętość prostopadłościanu wynosi: ' + str(volume))

prostopad(3,3,3)