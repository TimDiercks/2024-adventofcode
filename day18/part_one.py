test = False
filePath = './test_input.txt' if test else './input.txt'

dim = 7 if test else 71
with open(filePath, 'r') as f:
    data = f.read()

    corrupted_bytes = [list(map(int,row.split(","))) for row in data.split("\n")]
    map = [["." for _ in range(dim)] for _ in range(dim)]

fallen_bytes = 12 if test else 1024

for [x,y] in corrupted_bytes[:fallen_bytes]:
    map[y][x]= "#"

def add_tuple_elements(a: tuple[int, int], b: tuple[int,int]) -> tuple[int,int]:
    return (a[0]+b[0], a[1]+b[1])

def is_inside(pos: tuple[int, int]) -> bool:
    (x,y) = pos
    return x >= 0 and x < dim and y >= 0 and y < dim
directions = [(1,0), (-1,0), (0,1), (0,-1)]

start = (0, 0)
goal = (dim-1, dim-1)

queue = [(start, [])]
visited = set()
goal_path = []
while len(queue) != 0:
    (current_position, current_path) = queue.pop(0)
    if current_position in visited:
        continue
    if current_position == goal:
        goal_path = current_path
        break
    visited.add(current_position)
    for direction in directions:
        new_position = add_tuple_elements(current_position, direction)
        if not (is_inside(new_position) and map[new_position[1]][new_position[0]] != "#"):
            continue
        new_path = current_path + [current_position]
        queue.append((new_position, new_path))

print(f"Shortest path: {len(current_path)}")