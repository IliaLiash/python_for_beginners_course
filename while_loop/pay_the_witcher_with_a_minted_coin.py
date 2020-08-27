n = int(input())

count_1 = 0
count_5 = 0
count_10 = 0
count_25 = 0

while n // 25 >= 1:
    count_25 += 1
    n -= 25

while n // 10 >= 1:
    count_10 += 1
    n -= 10

while n // 5 >= 1:
    count_5 += 1
    n -= 5

while n // 1 >= 1:
    count_1 += 1
    n -= 1

print(count_25 + count_10 + count_5 + count_1)
