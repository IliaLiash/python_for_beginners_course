n = int(input())

while (((n // 10) // 10) //10) != 0:
    n = n //10
    
print(n % 10)
