import re
test = False
filePath = './test_input.txt' if test else './input.txt'

with open(filePath, 'r') as f:
    data = f.read()
    equations = [list(map(int, re.findall(r"\d+", line))) for line in data.split('\n')]


def generate_permutations(elements, length):
    if length == 0:
        return [[]]
    
    smaller_permutations = generate_permutations(elements, length - 1)
    permutations = []
    for perm in smaller_permutations:
        for element in elements:
            permutations.append(perm + [element])
    return permutations

def add(a,b):
    return a+b
def mult(a,b):
    return a*b
def concat(a,b):
    return int(str(a) + str(b))

operands = [add, mult, concat]

total_calibration_result = 0

for equation in equations:
    operand_permutations = generate_permutations(operands, len(equation)-2)
    for operations in operand_permutations:
        eq_res = equation[1:]
        for operation in operations:
            eq_res = [operation(*eq_res[:2])] + eq_res[2:]
            # Break early if already exceeds solution
            if eq_res[0] > equation[0]:
                break
        if eq_res[0] == equation[0]:
            total_calibration_result += eq_res[0]
            break

print(f"Total calibration result: {total_calibration_result}")