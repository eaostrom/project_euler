fh = open('input13.txt')
sum = 0
count = 0
for line in fh:
    line.rstrip()
    count += 1
    sum += int(line)
ssum = str(sum)
print(ssum[0:10])
