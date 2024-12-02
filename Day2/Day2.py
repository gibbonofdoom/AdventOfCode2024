import pathlib

input_file = pathlib.Path(__file__).parent.joinpath('input.txt')

reports = []
with input_file.open('r') as in_file:
    for line in in_file:
        reports.append(
            [int(i) for i in line.split()]
        )


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


safe_reports = 0
unsafe_reports = 0
for r in reports:

    if not all_ascending(r) and not all_descending(r):
        unsafe_reports += 1
        continue

    previous_value = r[0]
    unsafe = False
    for i in r[1:]:

        if i == previous_value:
            unsafe = True
            break

        if previous_value - 3 <= i <= previous_value + 3:
            previous_value = i
        else:
            unsafe = True
            break

    if not unsafe:
        safe_reports += 1

print(safe_reports)
