test = True
filePath = './test_input.txt' if test else './input.txt'

with open(filePath, 'r') as f:
    data = f.read()
    data_matrix = [list(line) for line in data.split('\n')]

dict = {}
for y in range(len(data_matrix)):
    for x in range(len(data_matrix[0])):
        node = data_matrix[y][x]
        if node in ".":
            continue
        if not node in dict:
            dict[node] = []
        dict[node].append((x,y))

for (node, positions) in dict.items():
    print(positions)