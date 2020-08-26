#The input is the number n and n lines, and then number k. Write a program that prints the k-th letter of the entered lines on one line without spaces.

n = int(input())
list_1 = []

for i in range(n):  #Создаем список
    s = input()
    list_1.append(s)

k = int(input())

for element in list_1:  #В созданном списке перебираем каждый элемент, который является строкой
    if len(element) < k:
        continue
    else:
        print(str(element[k-1]), end='')
