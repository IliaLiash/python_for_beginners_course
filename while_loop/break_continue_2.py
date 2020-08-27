num = int(input())

for i in range(1,num+1):
    if 5 <= i <= 9:
        continue
    if 17 <= i <= 37:
        continue
    if 78 <= i <= 87:
        continue
    else:
        print(i)
