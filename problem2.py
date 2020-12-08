#Fibonacci sequence
#First several terms: 1,2,3,5,8,13,34,55,89
#Find sum of even-valued terms under 4 million (inclusive)

fibonacci=[1,2]
for x in range(100000):
    x= fibonacci[x]+fibonacci[x+1]
    fibonacci.append(x)
 #this range is arbitrary. Hopefully it includes all values under 4 million.

result= []
for index_a,a in enumerate(fibonacci):
    if a <= 4000000:
        if a%2==0:
            result.append(a)
print(sum(result))
