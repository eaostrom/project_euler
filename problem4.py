#Find the largest palindrome made from the product of two 3-digit numbers.

largest = 1
for a in range(100,1000):
    for b in range(100,1000):
        s = str(a*b)
        if len(s)== 6:
            if s[0]==s[5] and s[1]==s[4]:
                if s[2]==s[3]:
                    if (a*b) > largest:
                        largest = a*b
print(largest)
