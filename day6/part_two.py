# Works for the test input but not for the whole
test = True
filePath = './test_input.txt' if test else './input.txt'

with open(filePath, 'r') as f:
    data = f.read()
    data_matrix = [list(line) for line in data.split('\n')]

def find_start_position():
    for y in range(len(data_matrix)):
        for x in range(len(data_matrix)):
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
    loop_positions = 0
    (x,y) = position
    move_direction = get_move_direction(data_matrix[y][x])
    
    while inside_matrix((x,y)):
        print_symbol = '+' if data_matrix[y][x] != "." else get_move_char(move_direction)
        data_matrix[y][x] = print_symbol
        did_turn = False
        if not inside_matrix((x+move_direction[0], y+move_direction[1])):
            break
        while data_matrix[y+move_direction[1]][x+move_direction[0]] == '#':
            move_direction = turn_right(move_direction)
            did_turn = True
            data_matrix[y][x] = '+'
        right = turn_right(move_direction)
        right_pos = (x+right[0], y+right[1])
        while inside_matrix(right_pos) and not did_turn:
            
            if data_matrix[right_pos[1]][right_pos[0]] in get_move_char(right):
                loop_positions += 1
                break
            if inside_matrix((right_pos[0]+right[0], right_pos[1]+right[1])) \
                and data_matrix[right_pos[1]][right_pos[0]] == "+"\
                and data_matrix[right_pos[1]+right[1]][right_pos[0]+right[0]] == "#":
                loop_positions += 1
                break
            right_pos = (right_pos[0]+right[0], right_pos[1]+right[1])
        
        x = x + move_direction[0]
        y = y + move_direction[1]
    return loop_positions
currentPosition = find_start_position()
loop_positions = move_through_field(currentPosition)
print(f"loop_positions: {loop_positions}")