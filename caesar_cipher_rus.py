n = int(input())
phraze = input().strip()
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
shifr = str()

for symbol in phraze:
    if symbol in ' ,.!?':
        shifr += symbol         
    elif 0 < alphabet.index(symbol.lower()) + n < len(alphabet):  #Если индекс не выходит за указанные рамки
        shifr += alphabet[alphabet.index(symbol.lower()) + n]   #Ищем индекс символа из фразы в алфавите и записываем в шифр
    else:
        shifr += alphabet[(alphabet.index(symbol.lower()) + n) % 32]    #Если индекс выходит

print('Result: ', '"', shifr, '"', sep='')
