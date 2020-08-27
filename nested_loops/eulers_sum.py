for a in range(1,150):
    for b in range(1,150):
        for c in range(1,150):
            for d in range(1,150):
                if a < b < c < d:
                    e = (a**5 + b**5 + c**5 + d**5)**0.2
                    if type(e) is int:
                        print(a + b + c + d + e)
                    else:
                        continue
