'''Напишите программу на Python для генерации 26 текстовых файлов с именами A.txt, B.txt и т. д. до Z.txt.'''

import os
import string


for i in string.ascii_uppercase:
    filename = "C:/Users/sulub/Documents/PP2_labs/Lab6/test_dir/" + i + ".txt"
    print(filename)
    with open(filename, "w") as file:
        file.write("text")
