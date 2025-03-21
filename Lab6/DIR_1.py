''' Напишите программу на Python для вывода списка только каталогов, 
 файлов и всех каталогов и файлов по указанному пути.'''
 

import os

if os.path.isdir("test_dir"):
    print("It is dir:", os.path.isdir("test_dir"))
else:
    print("It is not dir")
    
PP = os.listdir("test_dir")

direc = []
file_in = []

for i in PP:
    ff = os.path.join('test_dir', i)
    if os.path.isdir(ff):
        direc.append(i)
    elif os.path.isfile(ff):
        file_in.append(i)
        
for u in PP:
    
    print(u)
    

print(direc)
print(file_in)