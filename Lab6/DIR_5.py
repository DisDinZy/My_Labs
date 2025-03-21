'''Напишите программу на Python для записи списка в файл.'''

import os

my_list = ["apple", "banana", "cherry"]

with open("test_dir/fil1.txt", "w") as file:
    for i in my_list:
        file.writelines(i)
        file.write("\n")
    
with open("test_dir/fil1.txt", "r") as fik:
    print(fik.read())