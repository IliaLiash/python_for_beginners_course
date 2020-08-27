num = int(input())

while (num // 10) // 10 != 0: #until the number is two-digit
    num = num // 10
    
print(num % 10)
