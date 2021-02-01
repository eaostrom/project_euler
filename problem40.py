s = '.1'
n = 1
while n < 1000001:
    n += 1
    s += str(n)
first = int(s[1])*int(s[10])*int(s[100])*int(s[1000])
second = int(s[10000])*int(s[100000])*int(s[1000000])
print(first*second)
