#2520 is the smallest number that is evenly divisible by all integers 1-20
#Find the smallest number that is evenly divisible by ints 1-20
def evenly_divisible():
    ans = None
    i=20
    while i>1:
        i=i+2
        for n in range(11,21):
            if (i%n) > 0: break
            if n==20 and (i%n)==0:
                ans = i
                if ans is not None:
                    print(ans)
                    break
evenly_divisible()
