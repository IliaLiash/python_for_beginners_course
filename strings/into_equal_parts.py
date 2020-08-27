s = input()

from math import *

for k in range(ceil(len(s) / 2), len(s)):
    print(s[k], end='')
    
for i in range(ceil(len(s) / 2)):
    print(s[i], end='')
