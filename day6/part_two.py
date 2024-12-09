import copy
test = False
filePath = './test_input.txt' if test else './input.txt'

with open(filePath, 'r') as f:
    data = f.read()
    data_matrix = [list(line) for line in data.split('\n')]

def find_start_position():
    for y in range(len(data_matrix)):
        for x in range(len(data_matrix[0])):
            if(data_matrix[y][x] == "^"):
                return (x,y)
    print("Could not find start position")
    exit(1)

def get_move_direction(char: str) -> tuple[int, int]:
    match char:
        case "^":
            return (0,-1)
        case ">":
            return (1,0)
        case "v":
            return (0,1)
        case "<":
            return (-1,0)

def get_move_char(direction: tuple[int, int]) -> str:
    match direction:
        case (0,-1):
            return "^"
        case (1,0):
            return ">"
        case (0,1):
            return "v"
        case (-1,0):
            return "<"

def turn_right(direction: tuple[int, int]) -> tuple[int, int]:
    (x,y) = direction
    return (-y, x)

def inside_matrix(position: tuple[int, int]) -> bool:
    (x,y) = position
    return x >= 0 and y >= 0 and x < len(data_matrix[0]) and y < len(data_matrix)

def move_through_field(position):
    obsticals = set()
    (x,y) = position
    move_direction = get_move_direction(data_matrix[y][x])
    
    while inside_matrix((x,y)):
        print((x,y))
        print_symbol = '+' if not data_matrix[y][x] in ".^" else get_move_char(move_direction)
        data_matrix[y][x] = print_symbol

        start_pos = copy.deepcopy((x,y))
        loop_states = set()
        current_matrix = copy.deepcopy(data_matrix)
        if not inside_matrix((x+move_direction[0], y+move_direction[1])):
            break
        (next_x, next_y) = (start_pos[0]+move_direction[0], start_pos[1]+move_direction[1])
        if current_matrix[next_y][next_x] != "#":
            current_matrix[next_y][next_x] = "#"
            current_move_direction = turn_right(move_direction)
            while inside_matrix((x,y)):
                current_state = (x,y, *current_move_direction)
                if current_state in loop_states:
                    obsticals.add((next_y, next_x))
                    break
                loop_states.add(current_state)
                if not inside_matrix((x+current_move_direction[0], y+current_move_direction[1])):
                    break
                while current_matrix[y+current_move_direction[1]][x+current_move_direction[0]] == '#':
                    current_move_direction = turn_right(current_move_direction)
                x = x + current_move_direction[0]
                y = y + current_move_direction[1]

        (x, y) = start_pos
        if not inside_matrix((x+move_direction[0], y+move_direction[1])):
            break
        if data_matrix[y+move_direction[1]][x+move_direction[0]] == '#':
            move_direction = turn_right(move_direction)
            data_matrix[y][x] = '+'
            continue
        x = x + move_direction[0]
        y = y + move_direction[1]
    return obsticals

currentPosition = find_start_position()
obsticals = move_through_field(currentPosition)
for o in obsticals:
    print(o)
print(f"obsticals: {len(obsticals)}")