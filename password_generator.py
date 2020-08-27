from random import*

print('How many passwords do you want to generate?')
n = int(input())
print('Enter password length:')
password_len = int(input())

print('\n', 'Your passwords:', sep='')

def generate_password(lenght):
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    password = ''
    
    chars = digits + lowercase_letters + uppercase_letters + punctuation
    
    for symbol in ['i', 'l', '1', 'L', 'o', '0', 'O']:
        chars = chars.replace(symbol, '')
           
    for i in range(lenght):
        password += choice(chars)
    
    return password

for i in range(1, n + 1):
    print(i,'. ', generate_password(password_len), sep='', end='\n')
