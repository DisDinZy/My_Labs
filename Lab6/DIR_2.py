'''Напишите программу Python для проверки доступа к указанному пути. 
Проверьте существование, читаемость, записываемость и исполняемость указанного пути.'''

import os

ff = "test_dir"

print("Exist -", os.path.exists(ff))


if os.access(ff, mode=os.R_OK):
    print("Ready for read")
else:
    print("not ready for read")
if os.access(ff, mode=os.W_OK):
    print("Ready for write")
else:
    print("not ready for write")
if os.access(ff, mode=os.X_OK):
    print("Ready for execute")
else:
    print("not ready for execute")
