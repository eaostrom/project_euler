#Sum of the numbers on a clockwise spiral diagonal in a 1001x1001 grid.
sum = 1
sqsize = 1
spiral = 1

while sqsize < 1002:
    for item in range(1,5):
        spiral = spiral + (sqsize-1)
        if spiral != 1:
            sum += spiral
    sqsize = sqsize + 2
print(sum)
