s = input()
count = 0

for element in s:
    if element in '0123456789':
        count += 1
        
print(count)
