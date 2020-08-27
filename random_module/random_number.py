#How many tries to guess the number?
num = int(input())
count = 0

from math import*
print(int(ceil(log(num, 2))))