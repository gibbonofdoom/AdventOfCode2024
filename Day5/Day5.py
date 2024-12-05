import pathlib

input_file = pathlib.Path(__file__).parent.joinpath('input.txt')

lines = [
    line.strip() for line in input_file.open('r').readlines()
]

ordering_rules = {}
orders = []


def parse_file():

    global ordering_rules
    global orders

    read_ordering_rules = True

    for line in lines:
        if read_ordering_rules:
            if '|' not in line:
                read_ordering_rules = False
                continue
            before, after = line.split('|')
            before = int(before)
            after = int(after)
            if before not in ordering_rules:
                ordering_rules[before] = []
            ordering_rules[before].append(after)
            continue
        orders.append([int(x) for x in line.split(',')])


def check_order(order_input):
    for i, val in enumerate(order_input):
        for other in order_input[i+1:]:
            try:
                if other not in ordering_rules:
                    # this is fine
                    continue
                if val in ordering_rules[other]:
                    return False
            except KeyError as e:
                pass
    return True


def reorder_order(order_input):

    val_weights = {
        i: 0
        for i in order_input
    }

    for i, val in enumerate(order_input):
        for other in order_input[i+1:]:
            if other not in ordering_rules:
                continue
            if val in ordering_rules[other]:
                val_weights[val] += 1

    new_order = []
    for i in order[::-1]:
        new_order.insert(val_weights[i], i)
    return new_order


output_val = 0
output_incorrect_val = 0

parse_file()
for order in orders:
    if not check_order(order):
        order = reorder_order(order)
        output_incorrect_val += order[len(order) // 2]
        continue
    else:
        output_val += order[len(order) // 2]

print('PT1', output_val)
print('PT2', output_incorrect_val)
