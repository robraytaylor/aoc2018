values = open("Day 1\input.txt").readlines()
intValues = list(map(int, values))

""" Part 1 """

part1 = sum(intValues)
print("Part 1 Answer =  %s" % part1)

""" Part 2 """

index = 0
currentFrequency = 0
frequencies = []
while currentFrequency not in frequencies:
    frequencies.append(currentFrequency)
    currentFrequency += intValues[index % len(intValues)]
    """print(currentFrequency)"""
    index += 1

print("Part 2 Answer = %s" % currentFrequency)

