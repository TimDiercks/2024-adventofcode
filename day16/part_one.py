test = False
filePath = './test_input.txt' if test else './input.txt'

with open(filePath, 'r') as f:
    data = f.read()
    maze = [list(row) for row in data.split("\n")]

def get_start_pos(maze):
    for y in range(len(maze)):
        for x in range(len(maze)):
            if maze[y][x] != "S":
                continue
            return (x, y)

start_position = get_start_pos(maze)

def add_tuple_elements(a: tuple[int, int], b: tuple[int,int]) -> tuple[int,int]:
    return (a[0]+b[0], a[1]+b[1])

directions = [(1,0), (-1,0), (0,1), (0,-1)]
# cost, position, path, last_direction
queue = [(0, start_position, [], (1,0))]
visited = set()
path = None

while len(queue) != 0:
    min_score = -1
    min_id = -1
    for id, elem in enumerate(queue):
        if min_score == -1 or min_score > elem[0]:
            min_score = elem[0]
            min_id = id

    current_element = queue.pop(min_id)
    (current_cost, current_position, current_path, last_direction) = current_element
        
    visited.add(current_position)
    
    for direction in directions:
        new_position = add_tuple_elements(current_position, direction)
        # new_position will always stay inside bounds
        new_element = maze[new_position[1]][new_position[0]]
        if new_element == '#':
            continue
        if(new_position in visited):
            continue
        new_path = current_path + [current_position]
        new_cost = current_cost + 1
        if last_direction != direction:
            new_cost += 1000
        if new_element == 'E':
            path = (new_cost, new_path + [new_position])
            break
        queue.append((new_cost, new_position, new_path, direction))
    if path != None:
        break

min_score = path[0]
print(f"Score: {min_score}")