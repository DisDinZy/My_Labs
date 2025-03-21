'''Напишите программу на Python со встроенной функцией, которая возвращает True, если все элементы кортежа имеют значение True.'''

tuple_ = (1, 2, 3, 4, 0)
tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = (True, True, False)
tuple_3 = (1, 2, False, 4, 5)


print(all(tuple_))
print(all(tuple_1))
print(all(tuple_2))
print(all(tuple_3))
