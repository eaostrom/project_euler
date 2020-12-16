sumsq=0
sqsum=0
for n in range(1,101):
    sq = n**2
    sumsq = sumsq + sq
    sqsum = sqsum + n
sqsum = sqsum**2
print(sqsum-sumsq)
