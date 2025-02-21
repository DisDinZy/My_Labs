
def gen(n):
    for i in range(n):
        if(i % 2 == 0):
            yield i
        
        
N = int(input())
gena = gen(N)

fol = [ ]

for num in gena:
    fol.append(num)
    
print(fol)