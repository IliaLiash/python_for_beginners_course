#its length is at least 8 characters;
#it contains at least one uppercase letter (uppercase);
#it contains at least one lowercase letter (lowercase);
#it contains at least one digit.

def is_password_good(password):
    count = 0
    if len(password) >= 8:
        for i in range(len(password)):
            if password[i].islower() == True:
                count += 1
                break
        for k in range(len(password)):
            if password[k].isupper() == True:
                count += 1
                break
        for j in range(len(password)):
            if password[j].isdigit() == True:
                count += 1
                break
            
    if count == 3:
        return True
    else:
        return False

txt = input()

print(is_password_good(txt))
