my_list = list(map(int, input().split()))

a = max(my_list)
b = min(my_list)

for i in range(len(my_list)):
    if my_list[i] == max(my_list):
        my_list[i] = b
        break
       
for j in range(len(my_list)):
    if j == i:
        continue
    if my_list[j] == min(my_list):
        my_list[j] = a
        break
        
print(*my_list)
