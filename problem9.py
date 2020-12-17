r = range(1,1000)

for a in r:
    for b in r:
        for c in r:
            if a+b+c==1000 and a<b<c:
                if a**2 + b**2 == c**2:
                    print(a*b*c)
                    quit()
