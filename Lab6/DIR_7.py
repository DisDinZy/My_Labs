'''Напишите программу на Python для копирования содержимого файла в другой файл.'''

import os
import shutil

op = shutil.copy("test_dir/fil1.txt","test_dir/fil2.txt" )

with open("test_dir/fil2.txt") as file:
    print(file.read())