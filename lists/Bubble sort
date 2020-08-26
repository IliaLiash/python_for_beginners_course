a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]

n = len(a)
for i in range(n - 1):
    a_already_sort = True                   #Устанавливаем метку перед в цикле, перед вложенным циклом...
    for j in range(n - i - 1):              #... чтобы при каждом новом проходе метка возвразалась в True
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            a_already_sort = False
    if a_already_sort == True:
        break
print(a)
