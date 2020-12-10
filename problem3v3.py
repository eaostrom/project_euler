#Find the largest prime factor of 600851475143.
#The prime factors of 13195 are 5, 7, 13 and 29.

total = 600851475143

for num in range(1,total):
    if num > 1 and total% num ==0:
        factor= num
        #now check if this factor is prime
        for i in range(2, factor):
            if (factor % i) == 0:
                break
        else:
            print(num)
    else: continue
