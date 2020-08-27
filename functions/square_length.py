from math import*

def get_circle(radius):
    l = 2 * pi * radius
    s = pi * radius**2
    return l, s

r = float(input())

length, square = get_circle(r)
print(length, square)
