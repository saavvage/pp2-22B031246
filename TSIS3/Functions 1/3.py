""""
x = chickens
y = rabbits
"""

def solve(numheads, numlegs):
    for x in range(numheads + 1):   
        y = numheads - x            
        if 2*x + 4*y == numlegs:
            return x, y

numheads, numlegs = input().split()
numheads = int(numheads)
numlegs = int(numlegs)
print(solve(numheads, numlegs))