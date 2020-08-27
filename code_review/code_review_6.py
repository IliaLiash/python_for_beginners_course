#Product of the digits of the entered number

#Before
'''
n = input()
product = n % 10
while n >= 10:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)
'''

#After
n = int(input())
mult = 1
while n != 0:
    digit = n % 10
    mult *= digit
    n //= 10
print(mult)
