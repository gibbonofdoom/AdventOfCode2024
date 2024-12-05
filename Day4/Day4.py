from typing import Tuple, List
import pathlib
import re

input_file = pathlib.Path(__file__).parent.joinpath('input.txt')

lines = [
    line.strip() for line in input_file.open('r').readlines()
]

num_columns = len(lines[0])
num_rows = len(lines)

valid_matches = ['XMAS']


def lookup(x, y):

    starting_char = lines[y][x]

    vectors = [
        [0, -1],
        [1, -1],
        [1, 0],
        [1, 1],
        [0, 1],
        [-1, 1],
        [-1, 0],
        [-1, -1]
    ]

    potential_matches = []

    for vector in vectors:
        new_line = [starting_char]
        for i in range(1, 4):
            lookup_index_x = x + vector[0] * i
            lookup_index_y = y + vector[1] * i

            if lookup_index_x < 0 or lookup_index_y < 0:
                break

            try:
                new_line.append(lines[lookup_index_y][lookup_index_x])
            except IndexError as e:
                break

        potential_matches.append(''.join(new_line))

    return potential_matches


all_possible_matches = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        all_possible_matches.extend(lookup(j, i))

print(all_possible_matches)
print(all_possible_matches.count('XMAS'))



# for i, y in enumerate(lines):
#     for j, x in enumerate(y):



