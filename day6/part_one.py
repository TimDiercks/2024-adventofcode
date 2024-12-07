test = False
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

def turn_right(direction: tuple[int, int]) -> tuple[int, int]:
    (x,y) = direction
    return (-y, x)

def inside_matrix(position: tuple[int, int]) -> bool:
    (x,y) = position
    return x >= 0 and y >= 0 and x < len(data_matrix[0]) and y < len(data_matrix)

def move_through_field(position):
    (x,y) = position
    move_direction = get_move_direction(data_matrix[y][x])
    
    while inside_matrix((x,y)):
        data_matrix[y][x] = 'X'
        if not inside_matrix((x+move_direction[0], y+move_direction[1])):
            return
        while data_matrix[y+move_direction[1]][x+move_direction[0]] == '#':
            move_direction = turn_right(move_direction)
        x = x + move_direction[0]
        y = y + move_direction[1]

currentPosition = find_start_position()
move_through_field(currentPosition)
visited_positions = "".join("".join(row) for row in data_matrix).count('X')
print(f"visited_positions: {visited_positions}")