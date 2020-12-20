import math
x = ''
total = 0
def digit_fact(n):
    sum = 0
    for s in x:
        sums = math.factorial(int(s))
        sum += sums
    if sum == int(x):
        #print(sum)
        return True
    return False

n = 2
while True:
    n+= 1
    x = str(n)
    if digit_fact(n):
        total+= n
        print(total)
