'''Напишите программу на Python для подсчета количества строк в текстовом файле'''

import os

with open("test_dir/fil1.txt", "r") as file:
    op = file.readlines()
    
coint = len(op)
    
print(coint)

    