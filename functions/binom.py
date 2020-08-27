from math import*

def compute_binom(n, k):
    
    return int((factorial(n)) / (factorial(k) * (factorial(n - k))))


n = int(input())
k = int(input())

print(compute_binom(n, k))
