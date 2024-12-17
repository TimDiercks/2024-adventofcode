test = False
filePath = './test_input.txt' if test else './input.txt'

with open(filePath, 'r') as f:
    data = f.read()
    maze = [list(row) for row in data.split("\n")]

def get_start_pos(maze):
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] != "S":
                continue
            return (x, y)

start_position = get_start_pos(maze)

def add_tuple_elements(a: tuple[int, int], b: tuple[int,int]) -> tuple[int,int]:
    return (a[0]+b[0], a[1]+b[1])

directions = [(1,0), (-1,0), (0,1), (0,-1)]
# cost, position, path, last_direction
queue = [(0, start_position, [], (1,0))]
shortest = [[-1 for _ in range(len(maze[0]))] for _ in range(len(maze))]
paths = []

while len(queue) != 0:
    min_score = -1
    min_id = -1
    for id, elem in enumerate(queue):
        if min_score == -1 or min_score > elem[0]:
            min_score = elem[0]
            min_id = id
    current_element = queue.pop(min_id)
    (current_cost, current_position, current_path, last_direction) = current_element
    
    for direction in directions:
        if direction == (-last_direction[0], -last_direction[1]):
            continue
        new_position = add_tuple_elements(current_position, direction)
        # new_position will always stay inside bounds
        new_element = maze[new_position[1]][new_position[0]]
        if new_element == '#':
            continue
        new_path = current_path + [current_position]
        new_cost = current_cost + 1
        if last_direction != direction:
            new_cost += 1000
        
        # +1000 since some positions might not account for rotation to the next position
        if shortest[new_position[1]][new_position[0]] != -1 and shortest[new_position[1]][new_position[0]]+1000 < new_cost:
            continue
        shortest[new_position[1]][new_position[0]] = new_cost
        if new_element == 'E':
            paths.append((new_cost, new_path + [new_position]))
            break
        queue.append((new_cost, new_position, new_path, direction))

min_score = -1
min_id = -1
for id, elem in enumerate(paths):
    if min_score == -1 or min_score > elem[0]:
        min_score = elem[0]
        min_id = id
print(min_score)

for id in range(len(paths)-1,-1,-1):
    if paths[id][0] != min_score:
        print("remove")
        print(paths[id][0])
        del paths[id]

seats = set()
for path in paths:
    for pos in path[1]:
        seats.add(pos)

print(f"Seats: {len(seats)}")