#Find the sum of all the primes below two million.
import math
sum=0
total = 2000000
for num in range(2,total):
    for i in range(2,int(math.sqrt(num))+1):
        if (num % i) == 0:
            break
    else:
        sum+= num
print(sum)
