n = int(input())

from math import*

for i in range(1,floor(n/2)+1):
    print('*' * i)
    
print('*' * ceil(n/2))
    
for j  in range(floor(n/2),0,-1):
    print('*' * j)
