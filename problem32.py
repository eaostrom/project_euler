#Note: this is a general solution for numbers that are pandigital  1 to len(s)
#Line 18 makes it specific for 1-9 pandigital numbers
pandigital = {}
a = 1
for a in range(1,10000):
    for b in range(1,10000):
        c = a*b
        tup_ab, tup_c = (str(a)+str(b)), str(c)
        s = str(a)+str(b)+str(c)
        if len(s) >9: break
        count = 0
        for n in range(1,len(s)+1):
            sn = str(n)
            if sn in s:
                if s.count(sn)>1: break
            else: break
            count += 1
        if count == (len(s)):
            if len(s) == 9:
                pandigital[tup_c] = tup_ab
sum = 0
for items in pandigital:
    sum += int(items)
print(sum)
