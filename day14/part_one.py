import re
test = False
filePath = './test_input.txt' if test else './input.txt'

bathroom_size = (11,7) if test else (101, 103) 

with open(filePath, 'r') as f:
    data = f.read()
    regex = r"-*\d+"
    robots = [list(map(int, re.findall(regex, row))) for row in data.split("\n")]

def get_quadrant(robot):
    [x,y,_,_] = robot
    quadrant = 0
    if x == bathroom_size[0] // 2 \
        or y == bathroom_size[1] // 2:
        return None
    if x > bathroom_size[0] // 2:
        quadrant += 1
    if y > bathroom_size[1] // 2:
        quadrant += 2
    return quadrant

def move(robot):
    robot[0] += robot[2]
    robot[1] += robot[3]
    robot[0] %= bathroom_size[0]
    robot[1] %= bathroom_size[1]

for time in range(100):
    for i in range(len(robots)):
        move(robots[i])

robots_quadrants = [0,0,0,0]

for robot_id in range(len(robots)):
    quadrant = get_quadrant(robots[robot_id])
    if quadrant == None:
        continue
    robots_quadrants[quadrant] += 1

safety_factor = 1

for i in robots_quadrants:
    safety_factor *= i

print(robots_quadrants)
print(f"Safetyfactor: {safety_factor}")