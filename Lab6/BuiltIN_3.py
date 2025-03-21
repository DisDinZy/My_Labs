'''Напишите программу на Python со встроенной функцией, которая проверяет, является ли переданная строка палиндромом или нет.'''

sr = "madam"

if sr == ''.join(reversed(sr)):
    print(sr, "is polindrom")
else:
    print(sr, "Is not polindrom")