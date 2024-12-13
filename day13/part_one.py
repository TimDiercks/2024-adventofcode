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
    
    cheapest = (0,0)
    cheapest_cost = -1
    for A in range(101):
        B = (py-A*ay)/by

        if B < 0 or B%1 != 0 or float(A) != (px-B*bx)/ax:
            continue
        B = int(B)

        assert(A*ax+B*bx == px)
        assert(A*ay+B*by == py)
        
        current_cost = A*TOKENS_A+B*TOKENS_B
        if current_cost < cheapest_cost or cheapest_cost == -1:
            cheapest_cost = current_cost
            cheapest = (A, B)
            continue
        
    if cheapest != (0, 0):
        tokens += cheapest_cost

print(f"Total tokens: {tokens}")