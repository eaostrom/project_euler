fh = open('input11.txt')
m = []
#m represents matrix
for line in fh:
    line.rstrip()
    ints = line.split()
    for i in range(0, len(ints)):
        ints[i] = int(ints[i])
    m.append(ints)

row = 0
greatest = 0
while row < 20:
    c = 0
    #c represents count
    for i in m[row]:
        c += 1
        if c > 17: continue
        #a represents horizontal, left-right
        a = i * m[row][c] * m[row][c+1] * m[row][c+2]
        if a > greatest:
            greatest = a
        if row > 16: continue
        #b represents L to R downward diagonal
        b = i * m[row+1][c] * m[row+2][c+1] * m[row+3][c+2]
        if b > greatest:
            greatest = b
    row += 1

for c in range(20):
    for l in range(0, len(m)-3):
        #d represents vertical, up and down
        d = m[l][c]*m[l+1][c]*m[l+2][c]*m[l+3][c]
        if d > greatest:
            greatest = d
        if c < 3: continue
        #e represents L to R upward diagonal
        e = m[l][c] * m[l+1][c-1] * m[l+2][c-2] * m[l+3][c-3]
        if e > greatest:
            greatest = e
print(greatest)
