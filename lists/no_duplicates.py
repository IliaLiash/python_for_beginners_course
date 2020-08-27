#outputs only unique lines

n = int(input())
my_list1 = []

for i in range(n):
    s = input()
    if s not in my_list1:
        my_list1.append(s)

print(*my_list1,sep='\n')
