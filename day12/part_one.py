test = True
filePath = './test_input.txt' if test else './input.txt'

with open(filePath, 'r') as f:
    data = f.read()
    plant_map = list([list(line) for line in data.split('\n')])

w = len(plant_map[0])
h = len(plant_map)

visit_queue = [(x, y) for x in range(len(plant_map[0])) for y in range(len(plant_map))]
visited = set()

def is_inside_bounds(position):
    (x, y) = position
    return x >= 0 and y >= 0 and x < w and y < h   

directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
total_cost = 0
while len(visit_queue) != 0:
    area = 0
    circumference = 0
    innerQueue = [visit_queue.pop(0)]
    while len(innerQueue) != 0:
        area += 1
        (c_x, c_y) = innerQueue.pop(0)
        current_element = plant_map[c_y][c_x]
        visited.add((c_x, c_y))
        if (c_x, c_y) in visit_queue:
            visit_queue.remove((c_x, c_y))
        for (d_x, d_y) in directions:
            (n_x, n_y) = (c_x+d_x,c_y+d_y)
            if not is_inside_bounds((n_x,n_y)):
                circumference += 1
                continue
            new_element = plant_map[n_y][n_x]
            if new_element != current_element:
                circumference += 1
                continue
            if (n_x, n_y) in innerQueue or (n_x, n_y) in visited:
                continue
            innerQueue.append((n_x,n_y))
            
    total_cost += area*circumference

print(f"Total cost: {total_cost}")