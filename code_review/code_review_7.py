#Displays the sum of even digits of this number

#Before
'''
n = input()
s = 0
while n > 10:
    if n % 2 == 1:
        s = n % 10
    n //= 10
print(s)
'''

#After
n = int(input())
s = 0
while n != 0:
    if (n % 10) % 2 == 0:
        s += n % 10
    n //= 10
print(s)
