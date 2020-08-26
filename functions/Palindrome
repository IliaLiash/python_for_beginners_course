def is_palindrome(text):
    my_list1 = [i.lower() for i in text if i.lower() in 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя']
    my_list2 = [k.lower() for k in text[::-1] if k.lower() in 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя']
    flag = True
    
    for i in range(len(my_list1)):
        if my_list1[i] == my_list2[i]:
            continue
        else:
            flag = False
            
    return flag

txt = input()

print(is_palindrome(txt))
