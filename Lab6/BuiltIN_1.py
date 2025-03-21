'''Напишите программу на Python со встроенной функцией для умножения всех чисел в списке.'''

import functools
import operator

numbers = [2, 3, 4, 5]

f = functools.reduce(operator.mul, numbers)

print(f)


#или

'''
import functools

def mult(x, y):
    return x * y

numbers = [2, 3, 4, 5]

f = functools.reduce(mult, numbers)

print(f)

'''