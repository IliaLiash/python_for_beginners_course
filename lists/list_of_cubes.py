#Creates a list of their cubes from the specified numbers

n = int(input())
list1 = []

for i in range(n):
    digit = int(input())
    list1.append(digit**3)
    
print(list1)
