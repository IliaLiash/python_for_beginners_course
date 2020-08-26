num = int(input())
maxd = num % 10
mind = num % 10

while num != 0:
    last_digit = num % 10
    if last_digit > (num // 10) % 10 and last_digit > maxd:
        maxd = last_digit
    elif last_digit < mind:
            mind = last_digit
    num = num // 10
    
    
print('max digit =', maxd)
print('min digit =', mind)
