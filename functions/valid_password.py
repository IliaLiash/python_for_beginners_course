#a:b:c
#a - must be a palindrome;
#b - must be simple;
#c - must be even.

def is_valid_password(password):
    my_list = [i for i in password.split(':')]
    count = 0
    count_even = 0
    
    if my_list[0] == my_list[0][::-1]:
        count += 1
    
    for i in range(1, int(my_list[1]) + 1):
        if int(my_list[1]) % i == 0:
            count_even += 1
    if count_even == 2:
        count += 1
    
    if int(my_list[2]) % 2 == 0:
        count += 1
        
    if count == 3 and len(my_list) == 3:
        return True
    else:
        return False

psw = input()

print(is_valid_password(psw))
