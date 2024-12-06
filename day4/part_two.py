import re

test = False
filePath = './test_input.txt' if test else './input.txt'

xmas_occurrences = 0

with open(filePath, 'r') as f:
    data = f.read()
    data_matrix = [list(line) for line in data.split('\n')]

w_matrix = len(data_matrix[0])
h_matrix = len(data_matrix)

def find_recursive_mas(x, y, directions = [(-1,-1), (1,1), (1,-1), (-1,1)]) -> int:
    m_occurrences = 0
    s_occurrences = 0
    characters = []
    
    for (x_off, y_off) in directions:
        new_x = x + x_off
        new_y = y + y_off
        current_character = data_matrix[new_y][new_x]
        characters.append(current_character)
        if current_character == "M":
            m_occurrences += 1
        elif current_character == "S":
            s_occurrences += 1
    if not (m_occurrences == 2 and s_occurrences == 2):
        return 0
    if characters[0] == characters[1] or len(characters) < 4:
        return 0
    return 1

xmas_occurrences = 0

for y in range(1,len(data_matrix)-1):
    for x in range(1, len(data_matrix)-1):
        if data_matrix[y][x] != "A":
            continue
        
        xmas_occurrences += find_recursive_mas(x, y)

print(f"X-MAS occurrences: {xmas_occurrences}")