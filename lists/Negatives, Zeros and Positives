#Write a program that prints all negative numbers first, then zeros, and then all positive numbers, each on a separate line

n = int(input())
my_list_neg = []
my_list_zero = []
my_list_poz = []

for i in range(n):
    digit = int(input())
    if digit < 0:
        my_list_neg.append(digit)
    elif digit == 0:
        my_list_zero.append(digit)        
    elif digit > 0:
        my_list_poz.append(digit)

print(*my_list_neg,sep='\n')
print(*my_list_zero,sep='\n')
print(*my_list_poz,sep='\n')
