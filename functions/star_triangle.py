def draw_triangle():
    i = 1
    k = 7
    
    while i <= 15 and k >= 0:
        print(' '*k, '*'*(i - 1), '*'*i, sep='')
        k -= 1
        i += 1
        
draw_triangle()
