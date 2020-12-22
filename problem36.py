def doublebase_palindrome(s):
    bad = None
    for index in range(int((len(s)/2))):
        last = -(index+1)
        if s[index] == s[last]: continue
        else:bad = s

    if bad is None:
        binary = (bin(int(s)))
        b = (binary[2:])
        if b[0] != 0:
            for index in range(int((len(b)/2))):
                last = -(index+1)
                if b[index] == b[last]: continue
                else: bad = s
    if bad is None:
        return True

sum = 0
for i in range(1,1000000):
    s = str(i)
    if doublebase_palindrome(s):
        sum += int(s)
print(sum)
