import pathlib

input_file = pathlib.Path(__file__).parent.joinpath('input.txt')

lines = [
    line.strip() for line in input_file.open('r').readlines()
]

num_columns = len(lines[0])
num_rows = len(lines)

valid_matches = ['XMAS']


def get_entry(x, y, vector):
    return lines[y + vector[1]][x + vector[0]]


def lookup(x, y):

    starting_char = lines[y][x]
    if starting_char != 'A':
        return 0

    vectors = {
        'right_up': [1, -1],
        'right_down': [1, 1],
        'left_down': [-1, 1],
        'left_up': [-1, -1]
    }

    try:
        right_up_char = get_entry(x, y, vectors.get('right_up'))
        right_down_char = get_entry(x, y, vectors.get('right_down'))
        left_down_char = get_entry(x, y, vectors.get('left_down'))
        left_up_char = get_entry(x, y, vectors.get('left_up'))
    except IndexError as e:
        return 0

    x_one = f'{left_up_char}A{right_down_char}'
    x_two = f'{right_up_char}A{left_down_char}'

    count = 0
    for xmas in [x_one, x_two]:
        if xmas == 'MAS' or xmas[::-1] == 'MAS':
            count += 1

    if count == 2:
        print(x_one, x_two, x, y)

    return count == 2


total_count = 0
for i in range(1, num_rows):
    for j in range(1, num_columns):
        total_count += lookup(j, i)

print(total_count)


