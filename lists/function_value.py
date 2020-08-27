#f(x)=x**2 +2*x+1
#For each of the entered number x displays the value of the function each on a separate line

n = int(input())
my_list1 = []
my_list2 = []

for i in range(n):
    x = int(input())
    my_list1.append(x)
    
for element in my_list1:
    f = element**2 + 2*element + 1
    my_list2.append(f)
    
print(*my_list1,sep='\n')
print()
print(*my_list2,sep='\n')
