from typing import Tuple, List
import pathlib
import re


def iter_mul_values(string) -> List[Tuple: int]:
    search_string = r'mul\(\d{1,3},\d{1,3}\)'
    matches = re.findall(search_string, string)
    for match in matches:
        value_pair = []
        for i in re.findall(r'(\d+)', match):
            value_pair.append(int(i))
        yield value_pair


def get_do_matches(string):
    return re.findall(r"(?:(?<=^)|(?<=do\(\)))(.+?)(?=don't\(\)|$)", string)


input_file = pathlib.Path(__file__).parent.joinpath('input.txt')

reports = [
    line.strip() for line in input_file.open('r').readlines()
]
report = ''.join(reports)

result = 0
for do in get_do_matches(report):
    for x, y in iter_mul_values(do):
        result += x * y

print(result)

