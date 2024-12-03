import re

with open("Day03.txt") as f:
    data = f.read()


def part_1(data):
    total = 0
    for pair in re.findall(r"mul\((\d*),(\d*)\)", data):
        total += (int(pair[0]) * int(pair[1]))
    return total


print("======== Part 1 ========")
print(part_1(data))

