quantity = int(input())
largest = 0
previous_largest = 0

for i in range(quantity):
    num = int(input())
    if num > largest:
        previous_largest = largest
        largest = num
    elif num > previous_largest and num < largest:
        previous_largest = num
    
      
print(largest)
print(previous_largest)
