def bmi(w,h,s='K'):
    bmi = round(float(w) / (float(h) ** 2), 2)
    stan = ['Masz niedowagę.','Waga w normie.','Masz nadwagę.','Otyłość.']
    print('Twoje BMI wynosi: ' + str(bmi))
    if s == 'K':
        if bmi < 19:
            print(stan[0])
        elif bmi <= 27:
            print(stan[1])
        elif bmi <= 31:
            print(stan[2])
        else:
            print(stan[3])
    else:
        if bmi < 18.5:
            print(stan[0])
        elif bmi <= 25:
            print(stan[1])
        elif bmi <= 30:
            print(stan[2])
        else:
            print(stan[3])

bmi(55,1.66)
bmi(75,1.76,'M')
bmi(100,1.66)