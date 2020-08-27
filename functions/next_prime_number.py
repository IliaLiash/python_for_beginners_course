def get_next_prime(num):
    for i in range(num + 1, 10**6):
        count = 0                   #сбрасываем счетчик делителей перед переходом на каждое следующее число
        for j in range(1,i + 1):
            if i % j == 0:
                count += 1
        if count == 2:              #если делителей 2 - возвращаем число
            return i

n = int(input())

print(get_next_prime(n))
