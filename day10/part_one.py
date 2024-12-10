test = False
filePath = './test_input.txt' if test else './input.txt'

with open(filePath, 'r') as f:
    data = f.read()
    topo_map = list([list(map(int, line)) for line in data.split('\n')])

w = len(topo_map[0])
h = len(topo_map)

def is_in_bounds(position: tuple[int,int]):
    (x,y) = position
    return x >= 0 and x < w and y >= 0 and y < h

queue = []

# Put start positions into queue
for y in range(len(topo_map)):
    for x in range(len(topo_map[0])):
        if topo_map[y][x] == 0:
            queue.append((x,y, (x,y)))

trail_heads = set()

move_directions = [(0,1), (0,-1), (1,0), (-1,0)]
while len(queue) > 0:
    # print(queue)
    (current_x, current_y, start) = queue.pop(0)
    current_value = topo_map[current_y][current_x]
    for move_direction in move_directions:
        (new_x, new_y) = (current_x+move_direction[0], current_y+move_direction[1])
        if not is_in_bounds((new_x, new_y)):
            continue
        new_value = topo_map[new_y][new_x]
        if new_value != current_value + 1:
            continue
        if new_value == 9:
            trail_heads.add((new_x, new_y, start))
            continue
        if not (new_x, new_y, start) in queue:
            queue.append((new_x, new_y, start))
print(f"Trailhead scores: {len(trail_heads)}")