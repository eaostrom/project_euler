import math
x = math.factorial(100)
s = str(x)
sum = 0
for digit in s:
    i = int(digit)
    sum += i
print(sum)
