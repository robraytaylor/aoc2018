from itertools import groupby

def findCheckSumPart(x, o):
    groupedList = [list(g) for k, g in groupby(sorted(x))]
    return 1 if any(len(f) == o for f in groupedList) else 0

values = open("Day 2\input.txt").readlines()

checkSum2 = [findCheckSumPart(x, 2) for x in values]
checkSum3 = [findCheckSumPart(x, 3) for x in values]

checkSum = sum(checkSum2) * sum(checkSum3)

print("Part 1 Answer = %s" % checkSum)

