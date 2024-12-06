test = False
filePath = './test_input.txt' if test else './input.txt'

output_sum = 0

with open(filePath, 'r') as f:
    data = f.read()
    [ordering_rules, updates] = data.split('\n\n')
    ordering_rules = [list(map(int, rule.split('|'))) for rule in ordering_rules.split('\n')]
    updates = [list(map(int, update.split(","))) for update in updates.split("\n")]

def satisfies_ordering_rules(update):
    size = len(update)
    printed = []
    middle_page = 0 
    is_correct_update = True
    while len(update) != 0:
        page = update[0]
        correct_order = True
        for [first, second] in ordering_rules:
            if second == page and first in update:
                correct_order = False
                break

        if len(printed) > size // 2 and not is_correct_update:
            return printed[size // 2]
        if correct_order:
            printed.append(page)
            update.remove(page)
        else:
            is_correct_update = False
            update.remove(page)
            update.append(page)
            
    
    if is_correct_update:
        return 0
    return middle_page

for update in updates:
    output_sum += satisfies_ordering_rules(update)

print(f"sum: {output_sum}")