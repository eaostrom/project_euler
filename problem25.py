#Fibonacci sequence First 5 terms: 1,1,2,3,5
#The 12th term, 144, is the first to contain 3 digits
#What is the index of the first term to contain 1000 digits?

count= 3
prev = 1
current = 2
while current > 1:
    count = count+1
    next = prev + current
    prev = current
    current = next
    snex = str(next)
    if len(snex)== 1000:
        print(count)
        break
