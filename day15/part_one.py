test = False
filePath = './test_input.txt' if test else './input.txt'

WALL = '#'
BOX = 'O'
ROBOT = '@'
EMPTY = '.'

with open(filePath, 'r') as f:
    data = f.read()
    [warehouse, movements] = data.split("\n\n")

    warehouse = [list(row) for row in warehouse.split("\n")]
    movements = list("".join(["".join(row) for row in movements.split("\n")]))

def get_move_from_char(move_char: str):
    match(move_char):
        case "<":
            return (-1,0)
        case ">":
            return (1,0)
        case "^":
            return (0,-1)
        case "v":
            return (0,1)

def get_robot_position(
    warehouse: list[list[str]]
) -> tuple[int,int]:
    for y in range(len(warehouse)):
        for x in range(len(warehouse[0])):
            if warehouse[y][x] != ROBOT:
                continue
            return (x,y)

# Adds two tuples elementwise
def add_tuple_elements(a: tuple[int, int], b: tuple[int,int]) -> tuple[int,int]:
    return (a[0]+b[0], a[1]+b[1])

def get_element_by_tuple(matrix: list[list[str]], position: tuple[int,int]) -> None | str:
    w = len(matrix[0])
    h = len(matrix)
    (x, y) = position
    if x < 0 or x >= w or y < 0 or y >= h:
        return None
    return matrix[y][x]

def get_gps_coordinate(position: tuple[int,int]) -> int:
    return 100*position[1]+position[0]

def move_element(
    pos: tuple[int, int], 
    warehouse: list[list[str]], 
    move: tuple[int, int]
) -> tuple[0,0]:
    element_in_position = get_element_by_tuple(warehouse, pos)
    is_box = element_in_position == BOX
    expected_position = add_tuple_elements(pos, move)
    element_in_new_position = get_element_by_tuple(warehouse, expected_position)
    assert(element_in_new_position != None)
    if element_in_new_position == WALL:
        return pos
    if element_in_new_position == EMPTY:
        if is_box:
            warehouse[pos[1]][pos[0]] = EMPTY
            warehouse[expected_position[1]][expected_position[0]] = BOX
        return expected_position
    
    assert(element_in_new_position == BOX)
    # Move boxes recursively
    moved_box_position = move_element(expected_position, warehouse, move)
    
    if moved_box_position == expected_position: # Box could not be moved
        return pos
    
    if is_box:
        warehouse[pos[1]][pos[0]] = EMPTY
        warehouse[expected_position[1]][expected_position[0]] = BOX
    
    return expected_position
    

robot_pos = get_robot_position(warehouse)
# Remove from warehouse. This makes movement easier.
warehouse[robot_pos[1]][robot_pos[0]] = EMPTY    

for move in movements:
    robot_pos = move_element(robot_pos, warehouse, get_move_from_char(move))

gps_sum = 0
for y in range(len(warehouse)):
    for x in range(len(warehouse[0])):
        if warehouse[y][x] != BOX:
            continue
        gps_sum += get_gps_coordinate((x,y))
        
print(f"Sum of gps coordinates: {gps_sum}")