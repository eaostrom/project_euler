count = []
for a in range(2,101):
    for b in range(2,101):
        term = a**b
        if term not in count:
            count.append(term)
print(len(count))
