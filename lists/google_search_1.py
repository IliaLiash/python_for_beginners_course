#Displays all entered lines in which search word occurs

n = int(input())
my_list1 = []

for i in range(n):
    s = input()
    my_list1.append(s)

keyword = input().lower()

for element in my_list1:
    if keyword in element.lower():
        print(element, end='\n')
