test = True
filePath = './test_input.txt' if test else './input.txt'

with open(filePath, 'r') as f:
    data = f.read()
    file_matrix = [str(index // 2) if index % 2 == 0 else "." for (index, entry) in enumerate(map(int, data)) for _ in range(entry)]

new_position = 0
iter = len(file_matrix) -1
last_char = "."
file_size = 1
while iter >= 0:
    current_char = file_matrix[iter]
    if last_char == ".":
        file_size = 1
    elif last_char == current_char:
        file_size += 1
    else:
        # Sequence of file id ends
        free_space_start = -1
        for i in range(iter+1):
            replace_char = file_matrix[i]
            if(replace_char == "."):
                if(free_space_start == -1):
                    free_space_start = i
                continue
            if(free_space_start == -1):
                continue
            free_space_end = i
            space = free_space_end-free_space_start
            if space >= file_size:
                # Move to the front
                for j in range(free_space_start, free_space_start+file_size):
                    file_matrix[j] = last_char
                # Remove at the back
                for j in range(iter+1, len(file_matrix)):
                    if(file_matrix[j] == last_char):
                        file_matrix[j] = "."
                        continue
                    break
                break
            free_space_start = -1

        file_size = 1
    last_char = current_char
    iter -= 1

checksum = 0
for (index, file_id) in enumerate(file_matrix):
    if(file_id == "."):
        continue
    checksum += index*int(file_id)

print(f"checksum: {checksum}")
