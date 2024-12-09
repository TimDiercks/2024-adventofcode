test = False
filePath = './test_input.txt' if test else './input.txt'

with open(filePath, 'r') as f:
    data = f.read()
    file_matrix = [str(index // 2) if index % 2 == 0 else "." for (index, entry) in enumerate(map(int, data)) for _ in range(entry)]

new_position = 0
while True:
    while(new_position < len(file_matrix) and file_matrix[new_position] != "."):
            new_position += 1
    if(new_position >= len(file_matrix)):
         break
    shift_entry = file_matrix.pop()
    if(shift_entry == "."):
        continue
    file_matrix[new_position] = shift_entry
checksum = 0
for (index, file_id) in enumerate(file_matrix):
    checksum += index*int(file_id)

print(f"checksum: {checksum}")
