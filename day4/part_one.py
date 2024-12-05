import re

test = False
filePath = './test_input.txt' if test else './input.txt'

regex = r'(?=(XMAS|SAMX))'

xmas_occurrences = 0

with open(filePath, 'r') as f:
    data = f.read()

horizontal_xmas = re.findall(regex, data)
xmas_occurrences += len(horizontal_xmas)

data_matrix = [list(line) for line in data.split('\n')]

w_matrix = len(data_matrix[0])
h_matrix = len(data_matrix)

transposed = list(zip(*data_matrix))
transposed_data = '\n'.join(''.join(row) for row in transposed)

vertical_xmas = re.findall(regex, transposed_data)
xmas_occurrences += len(horizontal_xmas)

def get_next_expected_character(character):
    if character == "M":
        return "A"
    if character == "A":
        return "S"
    return None

def find_recursive_xmas(x, y, directions = [(-1,-1), (1,-1), (-1,1), (1,1)], expected_character = "M") -> int:
    local_occurrences = 0

    for (x_off, y_off) in directions:
        new_x = x + x_off
        new_y = y + y_off

        if new_x < 0 or new_x == w_matrix:
            continue
        if new_y < 0 or new_y == h_matrix:
            continue
        if data_matrix[new_y][new_x] != expected_character:
            continue
        print("")
        print(y+1,x+1, data_matrix[y][x])
        print(new_y+1,new_x+1, data_matrix[new_y][new_x])
        next_expected_character = get_next_expected_character(expected_character)
        if(next_expected_character == None):
            print("FOUND")
            return 1
        local_occurrences += find_recursive_xmas(new_x, new_y, [(x_off, y_off)], next_expected_character)

    return local_occurrences

xmas_occurrences = 0

for y in range(len(data_matrix)):
    for x in range(len(data_matrix)):
        if data_matrix[y][x] != "X":
            continue
        print("_______")
        print("")
        print(y+1,x+1, "X")
        
        xmas_occurrences += find_recursive_xmas(x, y)

print(f"XMAS occurrences: {xmas_occurrences}")