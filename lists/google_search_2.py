#Displays all entered lines, in which all search queries are found

n = int(input())
my_list1 = []
my_list2 = []

for i in range(n):            #создаем первый список
    s = input()
    my_list1.append(s)
    
k = int(input())

for j in range(k):            #создаем второй список
    key = input()
    my_list2.append(key)

for string in my_list1:        #вложенным циклом начинаем считать count... 
    count = 0                    #...обнуляя его перед каждым заходом в список слов-запросов
    for keyword in my_list2:
        if keyword.lower() in string.lower():
            count += 1
            if count >= k:
                print(string)
