def convert_to_python_case(text):
    my_list = [text[0].lower()]
    
    for i in range(1,len(text)):
        if text[i].islower() == True or text[i].isdigit() == True:
            my_list.append(text[i])
        elif text[i].isupper() == True and text[i-1].islower() == True:
            my_list.append('_' + text[i].lower())
            
    print(*my_list,sep='')

txt = input()

convert_to_python_case(txt)
