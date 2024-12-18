import re
import instructions as instr

test = False
filePath = './test_input.txt' if test else './input.txt'

with open(filePath, 'r') as f:
    data = f.read()
    A = int(re.findall(r"A:.(\d+)", data)[0])
    B = int(re.findall(r"B:.(\d+)", data)[0])
    C = int(re.findall(r"C:.(\d+)", data)[0])
    instructions = list(map(int,re.findall(r"Program:.(.+)", data)[0].split(",")))

assert(len(instructions) % 2 == 0)

output = []
As = [0]
correct_as = set()
while len(As) != 0:
    A = As.pop()
    for c in range(16):
        output = []
        register = [A+c,B,C]
        instruction_pointer = 0
        jumped = False

        while instruction_pointer < len(instructions)-1:
            instruction = instructions[instruction_pointer]
            operand = instructions[instruction_pointer+1]

            operation = instr.operations[instruction]
            (instruction_pointer, jumped, out) = operation(operand, register, instruction_pointer, jumped)
            if out != None:
                output.append(out)
    
        if "".join(list(map(str, instructions))).endswith("".join(list(map(str, output)))):
            if("".join(list(map(str, instructions))).startswith("".join(list(map(str, output))))):
                correct_as.add(A+c)
                continue
            As.append((A+c)*8)
            

print(f"Output: {min(correct_as)}")