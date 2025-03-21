'''Напишите программу Python для удаления файла по указанному пути. Перед удалением проверьте доступ и существование указанного пути.'''
#os.makedirs()  

import os

with open("test_dir/subdir1/test.txt", "w") as file:
    file.write("text")

if os.path.exists("test_dir/subdir1/test.txt"):
    if os.access("test_dir/subdir1/test.txt", mode=os.W_OK):
        os.remove("test_dir/subdir1/test.txt")
        print("File deleted")
else:
    print("Path doesn't exists")