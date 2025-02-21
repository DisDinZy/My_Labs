import random
import math

def squares(a, b):
    for i in range(a, b):
        yield i ** 2
        
        
N = random.randint(1, 50)
S = random.randint(50, 100)

num = squares(N, S)
fol = [ ]
 
for nus in num:
    fol.append(nus)

for i in fol:
    if i == (math.sqrt(i) * math.sqrt(i)):
        print(i)