waga = input('Podaj swoją wagę (w kilogramach): ')
wzrost = input('Podaj swój wzrost (w metrach): ')
bmi = float(waga) / (float(wzrost) ** 2)
print('Twoje BMI wynosi: ' + str(bmi))
