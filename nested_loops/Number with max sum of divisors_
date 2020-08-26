a = int(input())
b = int(input())
total = 0
max_total = 0
find_integer = 0

for i in range(a,b+1):   #начинаем перебор
    total = 0            #перед каждым повторением обнуляем сумму делителей, для нового подсчета с целью сравнения
    for j in range(1,i+1):  
        if i % j == 0:        #если число делитель....
            total += j        #...записываем его в сумму
            if total >= max_total:  #если сумма больше максимальной суммы (на первого шаге max_total == 0)...
                find_integer = i     #...записываем переменную в find_integer...
                max_total = total    #... a max_total присваиваем значением накопленной суммы total
print(find_integer, max_total)
