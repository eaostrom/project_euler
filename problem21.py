pairs = []
def d(total):
    dsum = 0
    for num in range(1,total):
        if total% num ==0:
            dsum += num
    pairs.append((total,dsum))
    if ((dsum,total)) in pairs:
        if dsum != total:
            return True

s = ''
amicable = 0
for n in range(1,10000):
   if d(n) is True:
       s = str(pairs[-1])
       pos = s.find(',')
       amicable += int(s[1:pos]) + int(s[pos+2:-1])
print(amicable)
