def is_correct_bracket(text):
    total = 0
    flag = True
        
    for i in range(len(text)):
        if total < 0:
            flag = False
            break
        if text[i] == '(':
            total += 1
        elif text[i] == ')':
            total -= 1
   
    if total != 0:
        flag = False
        

    return flag

txt = input()

print(is_correct_bracket(txt))
