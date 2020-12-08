#Fibonacci sequence
#First several terms: 1,2,3,5,8,13,34,55,89
#Find sum of even-valued terms under 4 million (inclusive)

result= []
prev = 1
current = 2
while current <= 4000000:
    next = prev + current
    prev = current
    current = next
    if prev%2==0:
        result.append(prev)
print(sum(result))
