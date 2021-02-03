last = ''
count = 0
for n in range (1,1001):
    letters = ''
    s = str(n)
    if len(s) > 1:
        if len(s) == 4: letters = 'onethousand'
        if len(s) == 3:
            if s[0] == '1': letters += 'onehundred'
            if s[0] == '2': letters += 'twohundred'
            if s[0] == '3': letters += 'threehundred'
            if s[0] == '4': letters += 'fourhundred'
            if s[0] == '5': letters += 'fivehundred'
            if s[0] == '6': letters += 'sixhundred'
            if s[0] == '7': letters += 'sevenhundred'
            if s[0] == '8': letters += 'eighthundred'
            if s[0] == '9': letters += 'ninehundred'
            if s[-2:] != '00': letters += 'and'
        if 10 < int(s[-2:]) < 20:
            if s[-2:] == '11': letters += 'eleven'
            if s[-2:] == '12': letters += 'twelve'
            if s[-2:] == '13': letters += 'thirteen'
            if s[-2:] == '14': letters += 'fourteen'
            if s[-2:] == '15': letters += 'fifteen'
            if s[-2:] == '16': letters += 'sixteen'
            if s[-2:] == '17': letters += 'seventeen'
            if s[-2:] == '18': letters += 'eighteen'
            if s[-2:] == '19': letters += 'nineteen'
            count += len(letters)
            print(letters)
            continue
        elif s[-2] == '1': letters += 'ten'
        elif s[-2] == '2': letters += 'twenty'
        elif s[-2] == '3': letters += 'thirty'
        elif s[-2] == '4': letters += 'forty'
        elif s[-2] == '5': letters += 'fifty'
        elif s[-2] == '6': letters += 'sixty'
        elif s[-2] == '7': letters += 'seventy'
        elif s[-2] == '8': letters += 'eighty'
        elif s[-2] == '9': letters += 'ninety'
    if s[-1] == '1': letters += 'one'
    if s[-1] == '2': letters += 'two'
    if s[-1] == '3': letters += 'three'
    if s[-1] == '4': letters += 'four'
    if s[-1] == '5': letters += 'five'
    if s[-1] == '6': letters += 'six'
    if s[-1] == '7': letters += 'seven'
    if s[-1] == '8': letters += 'eight'
    if s[-1] == '9': letters += 'nine'
    count += len(letters)
    print(letters)
print(count)
