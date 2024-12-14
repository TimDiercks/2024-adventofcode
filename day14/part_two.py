import re
test = False
filePath = './test_input.txt' if test else './input.txt'

bathroom_size = (11,7) if test else (101, 103) 

with open(filePath, 'r') as f:
    data = f.read()
    regex = r"-*\d+"
    robots = [list(map(int, re.findall(regex, row))) for row in data.split("\n")]

def move(robot):
    robot[0] += robot[2]
    robot[1] += robot[3]
    robot[0] %= bathroom_size[0]
    robot[1] %= bathroom_size[1]

elapsed_seconds = 0
while True:
    elapsed_seconds += 1
    positions = set()
    for i in range(len(robots)):
        move(robots[i])
        new = (robots[i][0],robots[i][1])
        if new in positions:
            continue
        positions.add(new)
    if len(positions) == len(robots):
        bathroom = [[0 for _ in range(bathroom_size[0])] for _ in range(bathroom_size[1])]
        for [x,y,_,_] in robots:
            bathroom[y][x] += 1
        print("\n".join(["".join(list(map(str, row))).replace("0", ".").replace("1", "#") for row in bathroom]))
        break

print(f"Elapsed_seconds: {elapsed_seconds}")