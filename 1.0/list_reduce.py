a = [[[[[[[[[['a'], 'b']]], 'c']]], 'd']], 'e']
b= [[[['s','t'],[['u']], 'v']],['w','x'],[[['y']],'z']]

def flatten(lista):
    flattened = []
    for element in lista:
        if type(element) == list:
            flattened.extend(flatten(element))
        else:
            flattened.append(element)
    return flattened
c = []
for i in range(10):
  c = [c, i]

print(flatten(a))
print(flatten(b))
print(c)
print(flatten(c))