#The method is based on the following "rule":
# 0.123123... = 123/999
# 0.714258714258... = 714258/999999 (=5/7) etc.

def f(denominator):
    x = 9
    z = x
    k = 1
    #k represents number of digits in recurring cycle
    while z % denominator:
        z = (z * 10) + x
        k += 1
    return k
#The while loop terminates only if there is a recurring decimal.

import math
def primes(n):
    for i in range(2, int(math.sqrt(n))+1):
        if (n % i) == 0:
            return False
    return True

for num in range(2,1000):
    if num == 2 or num == 5: continue
    if primes(num):
        print(num, f(num))
#The answer is the num with the largest k value.
