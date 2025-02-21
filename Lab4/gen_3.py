import random

def gen(n):
    for i in range(n):
        if(i % 3 == 0):
            yield i
            
def g(n):
    for o in range(n):
        if(o % 4 == 0):
            yield o
        
        
N = random.randint(10, 100)
gena = gen(N)
gea = g(N)

fol = [ ]
gol = [ ]

for num in gena:
    fol.append(num)

for nem in gea:
    gol.append(nem)
    
print(fol)
print(gol)




'''import random

def gen(n):
    for i in range(n):
        if(i % 3 == 0 or i % 4 == 0):
            yield i
        
        
N = random.randint(0, 100)
gena = gen(N)

fol = [ ]

for num in gena:
    fol.append(num)
    
print(fol)'''