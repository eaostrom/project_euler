#Find thirteen adjacent digits in the 1000-digit number (see input file) that have the greatest product.
#What is the value of this product?

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
