import re

test = False
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

similarityScore = sum([leftEntry * rightList.count(leftEntry) for leftEntry in leftList])

print(f"Similarity score: {similarityScore}")
