import re

test = False
filePath = './test_input.txt' if test else './input.txt'

xmas_occurrences = 0

with open(filePath, 'r') as f:
    data = f.read()
    data_matrix = [list(line) for line in data.split('\n')]

w_matrix = len(data_matrix[0])
h_matrix = len(data_matrix)

word_to_find = "MAS"
mas_a_locations = []

def find_recursive_mas(x, y, directions = [(-1,-1), (1,-1), (-1,1), (1,1)], current_word = "M") -> int:
    local_occurrences = 0
    if current_word == word_to_find:
        assert(len(directions) == 1)
        (x_off, y_off) = directions[0]
        a_pos = (x-x_off, y-y_off)
        in_list = a_pos in mas_a_locations
        if in_list:
            mas_a_locations.remove(a_pos)
            return 1
        
        mas_a_locations.append(a_pos)
        return 0
    elif not (current_word in word_to_find):
        return 0
    for (x_off, y_off) in directions:
        new_x = x + x_off
        new_y = y + y_off

        if new_x < 0 or new_x == w_matrix:
            continue
        if new_y < 0 or new_y == h_matrix:
            continue
        current_character = data_matrix[new_y][new_x]
        local_occurrences += find_recursive_mas(new_x, new_y, [(x_off, y_off)], current_word + current_character)
        
    return local_occurrences

xmas_occurrences = 0

for y in range(len(data_matrix)):
    for x in range(len(data_matrix)):
        if data_matrix[y][x] != "M":
            continue
        
        xmas_occurrences += find_recursive_mas(x, y)

print(f"X-MAS occurrences: {xmas_occurrences}")