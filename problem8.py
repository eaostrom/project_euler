length = 0
max = 1
fh = open('input8.txt')
inp = fh.read()
inp = inp.replace('\n','')

while length < len(inp):
    digits=(inp[length:length+13])
    length +=1
    prod = 1
    for s in digits:
        prod = prod*int(s)
    if prod<max: continue
    else: max = prod
print(max)

        #for d in lst:
        #    prod = prod*int(d)
        #rint(prod)
        #if prod > max:
        #    max = prod
#print(prod)
    #for i in range(len(line)):
    #    line[i] = int(line[i])
    #print(t)

        #adj= int(char)+int(char+1)+int(char+2)+int(char+3)
        #if adj > max:
        #    max = adj
#print(max)
