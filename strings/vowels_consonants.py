s = input()
count1 = 0
count2 = 0

for elem in s:
    if elem in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        count1 += 1
    if elem in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        count2 += 1

print('Количество гласных букв равно', count1)
print('Количество согласных букв равно', count2)
