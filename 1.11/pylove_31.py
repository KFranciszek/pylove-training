""" Docstring """


def podzielna(liczba, podzielna_przez):
    """ Docstring """
    return liczba % podzielna_przez == 0


def ugly(liczba):
    """ Docstring """
    if liczba == 1:
        return True
    for i in [2, 3, 5]:
        if podzielna(liczba, i):
            return True
    return False


print(ugly(11))
print(ugly(12))


def time(czas, jednostka):
    """ Docstring """
    h, m, s = czas.split(':')
    h = int(h)
    m = int(m)
    s = int(s)
    if jednostka == 's':
        return h * 3600 + m * 60 + s
    elif jednostka == 'm':
        return h * 60 + m + round(s / 60, 2)
    else:
        return h + round(m / 60, 2) + round(s / 3600, 2)


print(time('01:15:59', 's'))
print(time('01:15:59', 'm'))
print(time('01:15:59', 'h'))

result = []
r2 = []


def flatten(arr):
    """ Docstring """
    for el in arr:
        if isinstance(el, list):
            flatten(el)
        else:
            result.append(el)
    return result


def flatten_nr(arr):
    """ Docstring """
    while True:
        el = arr.pop()
        if not isinstance(el, list):
            r2.append(el)
        else:
            arr = el
        if arr:
            break
    return r2[::-1]


print(flatten([[[[[[[[[['a'], 'b']]], 'c']]], 'd']], 'e']))
print(flatten_nr([[[[[[[[[['a'], 'b']]], 'c']]], 'd']], 'e']))


def weird_power(a):
    """ Docstring """
    return a ** 2, a ** 3


def calculate(afun, data):
    """ Docstring """
    return afun(weird_power(data))


a = 3


# b = lambda a: sum(a)


def cokolwiek(aa):
    """ Docstring """
    return sum(aa)


b = cokolwiek(a)
c = calculate(b, a)
print(c)


def cokolwiek2(dd):
    """ Docstring """
    return sorted(dd)


d = cokolwiek2(a)
# d = lambda a: sorted(a)
f = calculate(d, a)
print(f)


def power_2(a):
    """ Docstring """
    return (a + 0.5 * a) ** 2


print(power_2(3))


def cokolwiek3(cc):
    """ Docstring """
    return (cc + 0.5 * cc) ** 2


x = cokolwiek(a)
# x = lambda a: (a + 0.5 * a) ** 2
print(x(3))


data = [(9, 0), (1, 2), (3, 4)]
sorted_data = sorted(data, key=lambda a: a[0], reverse=False)
max_data = max(data, key=lambda a: max(a))
min_data = min(data, key=lambda a: max(a))
filtered_data = list(filter(lambda a: sum(a) > 5, data))

print({
    'a': {
        'a': {
            'a': {
                'a': {
                    'a': {
                        'a': {
                            'a': {
                                'a': {
                                    'a': {'a': {'a': {'a': {'a': {'a': {
                        'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': {
                            'a': 1}}}}}}}}}}}}}}}}}}}}}}})
