a = [78, -32, 5, 3 -60, -64, -39, 60, -14, -62]
n = len(a)

for i in range(n - 1):
    for j in range (n - i - 1):
        b = max(a[:len(a) - j])
        c = a.index(b)
        a[len(a) - 1 - j], a[c] = a[c], a[len(a) - 1 - j]

print(a)
