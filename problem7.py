#First six prime numbers: 2,3,5,7,11,13. The 6th is 13.
#What is the 10 001st prime number?

def primelist():
    term=0
    highest = 0
    n=1
    while n >= 1:
        n= n + 1
        for i in range(2, n):
            if i>1:
                for num in range(2,i):
                    if (i % num) == 0:
                        break
                else:
                    if i> highest:
                        highest = i
                        term = term + 1
        if term==10001:
            print(i)
            break

primelist()
