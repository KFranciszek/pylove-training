def is_ugly(number):
    if number == 1 or number%2 == 0 or number % 3 == 0 or number % 5 == 0:
        return True
    else:
        return False

for i in range(0,25):
    print(str(i) + ' is ugly: ' + str(is_ugly(i)))