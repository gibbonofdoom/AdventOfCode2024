from typing import List
import pathlib


def all_ascending(items):
    prev = items[0]
    for i in items[1:]:
        if prev > i:
            return False
        prev = i
    return True


def all_descending(items):
    prev = items[0]
    for i in items[1:]:
        if prev < i:
            return False
        prev = i
    return True


def is_safe(items: List[int]):

    if not all_ascending(items) and not all_descending(items):
        return False

    previous_value = items[0]
    for i in items[1:]:

        if i == previous_value:
            return False

        if previous_value - 3 <= i <= previous_value + 3:
            previous_value = i
        else:
            return False

    return True


input_file = pathlib.Path(__file__).parent.joinpath('input.txt')

with input_file.open('r') as in_file:
    reports = [
        [
            int(i)
            for i in line.split()
        ]
        for line in in_file
    ]


safe_reports = 0
for r in reports:

    if is_safe(r):
        safe_reports += 1
        continue

    # drop items in turn until we get a safe report
    for i in range(len(r)):
        _r = r[::]  # clone list
        _r.pop(i)
        if is_safe(_r):
            safe_reports += 1
            break


print('#:', safe_reports)
