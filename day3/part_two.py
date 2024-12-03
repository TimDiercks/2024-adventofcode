import re

test = False
filePath = './test_input.txt' if test else './input.txt'

regex = r'((mul\(\d+,\d+\))|(don\'t\(\))|(do\(\)))'

with open(filePath, 'r') as f:
    data = f.read()
    data = data.replace('\n', '')
    instructions = re.findall(regex, data)
    instructions = [first for (first, _, _, _) in instructions]

enabled = True

def result_from_mul_string(input: str) -> int:
    global enabled
    if(input == "don't()"):
        enabled = False
        return 0
    if(input == "do()"):
        enabled = True
        return 0
    if(not enabled):
       return 0
    input = input.replace('mul(', '').replace(')', '')
    numbers = list(map(int, input.split(",")))
    return numbers[0]*numbers[1]

total_sum = sum([result_from_mul_string(instruction) for instruction in instructions])
print(f"Total sum: {total_sum}")