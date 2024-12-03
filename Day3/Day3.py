from typing import Tuple, List
import pathlib
import re

input_file = pathlib.Path(__file__).parent.joinpath('input.txt')

reports = [
    line for line in input_file.open('r').readlines()
]


def iter_mul_values(string) -> List[Tuple: int]:

    search_string = r'mul\(\d{1,3},\d{1,3}\)'
    matches = re.findall(search_string, string)
    for match in matches:
        value_pair = []
        for i in re.findall(r'(\d+)', match):
            value_pair.append(int(i))
        yield value_pair


def do_calc(value: Tuple[int]) -> int:
    return value[0] * value[1]


result = 0
for report in reports:
    for pair in iter_mul_values(report):
        result += do_calc(pair)
print(result)
