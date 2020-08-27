def is_magic(date):
    my_list = [int(i) for i in date.split('.')]
    
    return my_list[0] * my_list[1] == my_list[2] % 100
    
date = input()

print(is_magic(date))
