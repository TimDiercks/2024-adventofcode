import re

test = True
filePath = './test_input.txt' if test else './input.txt'

regex = r'\s+'

with open(filePath, 'r') as f:
    data = f.read()
    data = data.split('\n')
    data = [d for d in data if len(d) > 0]

    leftList, rightList = zip(*[re.split(regex, d) for d in data])
    leftList = list(map(int, leftList))
    rightList = list(map(int, rightList))

assert(len(leftList) == len(rightList))

leftList.sort()
rightList.sort()

totalDistance = sum([abs(rightEntry-leftEntry) for leftEntry, rightEntry in zip(leftList, rightList)])

print(f"Total distance: {totalDistance}")