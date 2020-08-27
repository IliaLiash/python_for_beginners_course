s = input().split()
total = 0
my_list1 = []

for element in s:
    total += int(element)
    my_list1.append(element)

print(*my_list1,sep='+', end='=')
print(total)
