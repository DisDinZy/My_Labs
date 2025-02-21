import random

def donul(a):
    for i in range(a, -1, -1):
        yield i
        
        
        
a = random.randint(1, 100)
num = donul(a)

fol = [ ]

for i in num:
    fol.append(i)
    
    
print(fol)