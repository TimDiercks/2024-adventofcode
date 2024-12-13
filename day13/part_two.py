import re

test = False
filePath = './test_input.txt' if test else './input.txt'

with open(filePath, 'r') as f:
    data = f.read()
    regex = r"X.(\d+).+Y.(\d+)"
    machines = [re.findall(regex, s) for s in data.split("\n\n")]
    machines = [[(int(a), int(b)) for (a,b) in machine] for machine in machines]
    # Now we have a list of 3 tuples containing x and y coordinates of [buttonA, buttonB, prize]
    
TOKENS_A = 3
TOKENS_B = 1

tokens = 0
for machine in machines:
    (ax, ay) = machine[0]
    (bx, by) = machine[1]
    (px, py) = machine[2]
    px += 10000000000000
    py += 10000000000000
    B = (px*ay-py*ax)/(bx*ay-by*ax)
    A = (px-B*bx)/ax

    if B % 1 == 0 and A % 1 == 0:
        tokens += B*TOKENS_B+A*TOKENS_A

print(f"Total tokens: {tokens}")