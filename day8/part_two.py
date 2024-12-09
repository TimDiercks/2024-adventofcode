test = False
filePath = './test_input.txt' if test else './input.txt'

with open(filePath, 'r') as f:
    data = f.read()
    data_matrix = [list(line) for line in data.split('\n')]

w = len(data_matrix[0])
h = len(data_matrix)
dict = {}
for y in range(h):
    for x in range(w):
        node = data_matrix[y][x]
        if node in ".":
            continue
        if not node in dict:
            dict[node] = []
        dict[node].append((x,y))

def is_in_bounds(position: tuple[int,int]):
    (x,y) = position
    return x >= 0 and x < w and y >= 0 and y < h

def add_anti_nodes(nodes: set[tuple[int,int]], set: set[tuple[int,int]]):
    for node in nodes:
        if is_in_bounds(node):
            set.add(node)

anti_node_positions = set()

for (node, positions) in dict.items():
    for pos1_index in range(len(positions)-1,-1,-1):
        (x1, y1) = positions[pos1_index]
        positions.remove((x1, y1))
        for pos2_index in range(len(positions)-1,-1,-1):
            (x2, y2) = positions[pos2_index]
            (vec_x, vec_y) = (x2-x1, y2-y1)
            anti_nodes = set()
            (x3,y3) = (x1,y1)
            while is_in_bounds((x3, y3)):
                anti_nodes.add((x3, y3))
                x3 = x3+vec_x
                y3 = y3+vec_y
            (x3,y3) = (x1,y1)
            while is_in_bounds((x3, y3)):
                anti_nodes.add((x3, y3))
                x3 = x3-vec_x
                y3 = y3-vec_y
            add_anti_nodes(anti_nodes, anti_node_positions)

print(f"Anti nodes: {len(anti_node_positions)}")