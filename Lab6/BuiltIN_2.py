'''Напишите программу на Python со встроенной функцией, которая принимает строку и подсчитывает количество заглавных и строчных букв.'''

input_string = "Hello World!"

count_up = 0
count_low = 0

for i in input_string:
    if i.isupper():
        count_up = count_up + 1
    if i.islower():
        count_low = count_low + 1 
        
print("Upper =", count_up)
print("Lower =", count_low)