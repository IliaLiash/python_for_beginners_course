num = int(input())
flag = True

while (num // 10) // 10 != 0 and flag != False:
        if num % 10 == (num // 10) % 10:
            flag = True
            num = num // 10
        else:
            flag = False
if flag == True and (num % 10 == num // 10):
    print('YES')
elif num // 10 == 0:
    print('YES')
elif (num // 10) // 10 == 0 and (num % 10 != num // 10):
    print('NO')
else:
    print('NO')
