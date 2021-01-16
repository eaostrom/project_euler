ans = 0
for num in range(1000,1000000):
    sum = 0
    s = str(num)
    for digit in s:
        i = int(digit)
        sum += i**5
    if sum == num:
        ans += sum
print(ans)
