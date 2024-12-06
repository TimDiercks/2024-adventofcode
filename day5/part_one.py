test = False
filePath = './test_input.txt' if test else './input.txt'

output_sum = 0

with open(filePath, 'r') as f:
    data = f.read()
    [ordering_rules, updates] = data.split('\n\n')
    ordering_rules = [list(map(int, rule.split('|'))) for rule in ordering_rules.split('\n')]
    updates = [list(map(int, update.split(","))) for update in updates.split("\n")]

def satisfies_ordering_rules(update):
    printed = []

    for page in update:
        correct_order = True
        for [first, second] in ordering_rules:
            if first == page and second in printed:
                correct_order = False
                break
        if correct_order:
            printed.append(page)
        else:
            return 0
    return update[len(update) // 2] 

for update in updates:
    output_sum += satisfies_ordering_rules(update)

print(f"sum: {output_sum}")