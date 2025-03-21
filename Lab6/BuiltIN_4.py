'''Напишите программу на Python, которая вызывает функцию квадратного корня через определенные миллисекунды.'''
import math
import time

a = int(input("Num: "))
b = int(input("Millisec: "))

time.sleep(b / 1000)
f = math.sqrt(a)
print(f"Square root of {a} after {b} miliseconds is {f}")