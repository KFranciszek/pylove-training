import random
for i in range(9):
    print(' ' *(9 - i) + '/' *(i + 1) + '\\' * (i + 1))

print(' ' *9 + '*')
for i in range(9):
    line = ' ' * (9 - i) +  '/' * (i + 1) + '\\' * (i + 1)
    ball = int(random.random()*i)
    if ball != 0:
        line = list(line)
        line[ball + 9 - i] = '*'
        line = ''.join(line)
    print(line)