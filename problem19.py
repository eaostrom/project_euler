year = range(1,366)
total = 0
Sun = 1
date = 1900
count = 0
century = range(100)

for years in century:
    date += 1
    for day in year:
        jan = 0
        feb = jan + 31
        if date % 4 == 0 and date!= 1900:
            mar = feb + 29
        else: mar = feb + 28
        apr = mar + 31
        may = apr + 30
        jun = may + 31
        jul = jun + 30
        aug = jul + 31
        sep = aug + 31
        oct = sep + 30
        nov = oct + 31
        dec = nov + 30
        first = [jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec]
        Sun += 1
        if Sun % 7 == 0:
            Sun -= 7
        if (day-1) in first:
            if Sun == 0:
                count += 1
print(count)
