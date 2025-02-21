import random

def gen(n):
    for i in range(n + 1):
        yield i **2
        
        
N = random.randint(1, 10)
gena = gen(N)

print("Digit -", N)
for num in gena:
    print(num) 