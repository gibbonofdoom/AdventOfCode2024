import pathlib


def parse_file():

    input_file = pathlib.Path(__file__).parent.joinpath('input.txt')

    left_items = []
    right_items = []

    for line in input_file.open('r'):
        x, y = line.split()
        left_items.append(int(x))
        right_items.append(int(y))

    left_items.sort()
    right_items.sort()

    return left_items, right_items


def get_similarity_score(item, list_to_check):
    count = list_to_check.count(item)
    return item * count


left_items, right_items = parse_file()

similarity_score = 0
for i in left_items:
    similarity_score += get_similarity_score(i, right_items)

print(similarity_score)
