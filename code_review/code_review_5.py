#Displays the first digit

#Before
'''
n = int(input())
while n > 0:
    n %= 10
print(n)
'''


#After
n = int(input())

while (n //10 != 0):
    n //= 10
    
print(n)
