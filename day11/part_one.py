test = False
filePath = './test_input.txt' if test else './input.txt'

remaining_blinks = 25

with open(filePath, 'r') as f:
    data = f.read()
    stone_list = list(map(int,data.split(" ")))

def get_new_stones(stone: int) -> list[int]:
    stone_string = f"{stone}"
    if stone == 0:
        return [1]
    if len(stone_string) % 2 == 0:
        half_length = len(stone_string) // 2
        return [int(stone_string[:half_length]), int(stone_string[half_length:])]
    return [stone*2024]

def blink(stone_list: list[int]):
    for index in range(len(stone_list)-1, -1, -1):
        new_stones = get_new_stones(stone_list[index])
        del stone_list[index]
        for (sub_index,new_stone) in enumerate(new_stones):
            stone_list.insert(index + sub_index, new_stone)

while remaining_blinks > 0:
    blink(stone_list)
    remaining_blinks -= 1    
print(f"Amount of stones: {len(stone_list)}")