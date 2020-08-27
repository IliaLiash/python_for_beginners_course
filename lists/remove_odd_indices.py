#Creates list from the specified numbers, then removes all elements at odd indices

n = int(input())
list_1 = []

for i in range(n):
    digit = int(input())
    list_1.append(digit)

del list_1[1::2]

print(list_1)
