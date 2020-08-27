s = input()

for elem in s:
    if elem in '0123456789':
        print('Цифра')
        break
else:
    print('Цифр нет')
