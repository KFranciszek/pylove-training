def not_uniq_list(lista):
    if type(lista) != list:
        raise ValueError
    for elem in lista:
       if type(elem) != int and type(elem) != str:
           raise ValueError
    return [elem for elem in lista if lista.count(elem) > 1]


print(not_uniq_list([3, 1, 3, 1, 2]))
print(not_uniq_list([{2: 'fghjj'}, 2, 4, 3, 1, 3, 1, 2]))
print(not_uniq_list(['44', '44', '5567jk', 3, 1, 3, 1, 2]))
print(not_uniq_list([3, 1, 3, 1, 2, 3, 6, 7, 1]))
print(not_uniq_list([1, 2, 3, 1, 3]))
print(not_uniq_list([9]))
print(not_uniq_list([]))
# print(not_uniq_list('ala'))