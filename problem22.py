fh = open('names.txt')
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

term = 0
total = 0
for line in fh:
    line.rstrip()
    names = line.split(',')
    order = sorted(names)
    for name in order:
        term += 1
        alphavalue = 0
        for letter in name:
            if letter in alpha:
                result = alpha.find(letter) + 1
                alphavalue += result
        total += (term * alphavalue)
print(total)
