paths = []

def trial():
    s = ''
    import random
    while len(s) < 10:
        down = s.count('0')
        right = s.count('1')
        if down == 5:
            s = s + '1'
            continue
        if right == 5:
            s = s + '0'
            continue
        flip = random.randint(0,1)
        if len(s) < 10:
            s = s + str(flip)
    return s

for t in range(1,100000):
    x = trial()
    if x not in paths:
        paths.append(x)
print(len(paths))
