#Displays the maximum digit of number, multiple of 3
#Before
'''
n = int(input())
max_digit = n % 10
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit < max_digit:
            digit = max_digit
    n = n % 10
if max_digit == 0:
    print('NO')
else:
    print(max_digit)
'''

#After
n = int(input())
max_digit = 1

while n != 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
        if digit == 0:
            max_digit = 0
    n //= 10
    
if max_digit % 3 == 0:
    print(max_digit)
else:
    print('NO')
