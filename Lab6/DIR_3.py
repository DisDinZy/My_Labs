'''Напишите программу Python для проверки существования заданного пути.
Если путь существует, найдите часть имени файла и каталога заданного пути.'''

import os

if(os.path.exists("test_dir")):
    print("Path exists")
    base = os.path.basename("test_dir/file1.txt")
    direc = os.path.dirname("test_dir/file1.txt")
    print(base)
    print(direc)
    
else:
    print("Path doesn't exists")