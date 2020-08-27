#Line-by-line output
'''
s_list = input().split()

for element in s_list:
    print(element, end='\n')
'''

#Initials
#Владимир Семенович Высоцкий
'''
s_list = input().split()

for element in s_list:
    print(element[0] + '.', end='')
'''

#Split
'''
s = input()

words = s.split('\\')
for element in words:
    print(element, end='\n')
'''

#Diagram
'''
s_list = input().split()

for i in range(len(s_list)):
    s_list[i] = int(s_list[i])

for element in s_list:
    print(element * '+', end='\n')
'''

#Correct ip address
'''
s_list = input().split('.')

for i in range(len(s_list)):
    s_list[i] = int(s_list[i])

flag = True
for element in s_list:
    if 0 <= element <= 255:
        continue
    else:
        flag = False
        break
if flag == True:
    print('YES')
else:
    print('NO')
'''

#Add separator
'''
s = input()
symbol = input()

chars=list(s)           #получаем список из элементов строки
s = symbol.join(chars)  #склеиваем его указанным символом
print(s)
'''
