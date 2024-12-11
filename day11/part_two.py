import re
test = False
filePath = './test_input.txt' if test else './input.txt'

remaining_blinks = 75
stones = {}

with open(filePath, 'r') as f:
    data = f.read()
    stone_list = data.split(" ")
    for stone in stone_list:
        if(stone in stones):
            stones[stone] += 1
            continue
        stones[stone] = 1

def push_or_add(stone, amount, stones):
    if stone in stones:
        new_stones[stone] += amount
    else:
        new_stones[stone] = amount

while remaining_blinks > 0:
    new_stones = {}
    for stone in stones.keys():
        amount_stones = stones[stone]
        if stone == "0":
            push_or_add("1", amount_stones, new_stones)
        elif len(stone) % 2 == 0:
            half_length = len(stone) // 2
            left = stone[:half_length]
            right = re.sub(r"^0+(?!\b)", "", stone[half_length:])
            push_or_add(left, amount_stones, new_stones)
            push_or_add(right, amount_stones, new_stones)
        else:
            new_gem = str(int(stone)*2024)
            push_or_add(new_gem, amount_stones, new_stones)

    stones = new_stones
    remaining_blinks -= 1

    
print(f"Amount of stones: {sum([stones[key] for key in stones.keys()])}")