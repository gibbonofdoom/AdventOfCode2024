import pathlib

input_file = pathlib.Path(__file__).parent.joinpath('input.txt')

left_items = []
right_items = []

for line in input_file.open('r'):
    x, y = line.split()
    left_items.append(int(x))
    right_items.append(int(y))

left_items.sort()
right_items.sort()

diff = 0
for i, left_item in enumerate(left_items):
    right_item = right_items[i]
    this_diff = abs(left_item - right_item)
    diff += this_diff

print(diff)
