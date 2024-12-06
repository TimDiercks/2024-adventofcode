import re

test = False
filePath = './test_input.txt' if test else './input.txt'

xmas_occurrences = 0

with open(filePath, 'r') as f:
    data = f.read()
    data_matrix = [list(line) for line in data.split('\n')]

w_matrix = len(data_matrix[0])
h_matrix = len(data_matrix)

word_to_find = "XMAS"

def find_recursive_xmas(x, y, directions = [(-1,-1), (1,-1), (-1,1), (1,1), (1,0), (-1,0), (0,1), (0,-1)], current_word = "X") -> int:
    local_occurrences = 0
    if current_word == word_to_find:
        return 1
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
        local_occurrences += find_recursive_xmas(new_x, new_y, [(x_off, y_off)], current_word + current_character)

    return local_occurrences

xmas_occurrences = 0

for y in range(len(data_matrix)):
    for x in range(len(data_matrix)):
        if data_matrix[y][x] != "X":
            continue
        
        xmas_occurrences += find_recursive_xmas(x, y)

print(f"XMAS occurrences: {xmas_occurrences}")