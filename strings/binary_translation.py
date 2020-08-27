s = int(input())
d2 = ''

while s > 0:
    d2 += str(s % 2)
    s = s // 2

print(d2[::-1])
