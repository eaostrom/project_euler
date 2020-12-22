maxsteps = 1
count = 1
for n in range(2,1000000):
    steps = 1
    count += 1
    while True:
        if n==1:
            if steps > maxsteps:
                maxsteps = steps
                start = count
            break
        elif n%2==0:
            n = int(n/2)
            steps+=1
            continue
        elif n%2==1:
            n = 3*n + 1
            steps+=1
            continue
print('start:',start,'maxsteps:',maxsteps)
