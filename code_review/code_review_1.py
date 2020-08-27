#Number of non-negative numbers in the sequence and their product


#Before
count = 0
p = 0
for i in range(1, 10):
    x = int(input())
    if x > 0:
        p = p * x
        count = count + 1
if count > 0:
    print(x)
    print(p)
else:
    print('NO')
    
    
#After
count = 0
p = 1
for i in range(1, 11):
    x = int(input())
    if 0 <= x <= 10**6:
        p = p * x
        count += 1
    if -(10**6) <= x < 0:
        continue
        
if count > 0:
    print(count)
    print(p)
else:
    print('NO')
