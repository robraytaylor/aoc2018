from itertools import groupby

def removeCharAtIndex(s, i):
    return s[0:i] + s[i+1:]

values = [s[:-1] for s in open("Day 2\input.txt").readlines()]

#values = ["abzde", "abcde", "fgh21"]
#values = ["abcde","fghij","klmno","pqrst","fguij","axcye","wvxyz"]

result = ""
for idx, val in enumerate(values[0]):  
    groupedList = [list(g) for k, g in groupby(sorted([removeCharAtIndex(x, idx) for x in values]))]
    print(groupedList)
    if(any(len(f) == 2 for f in groupedList)):
        result = next(f[0] for f in groupedList if len(f) == 2)
        break

print("Part 2 Answer = %s" % result)

