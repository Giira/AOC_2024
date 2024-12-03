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


def part_2(data):
    data = data.split("don't()")
    new_data = []
    for i in range(len(data)):
        if i == 0:
            new_data.append(data[i])
        else:
            tmp = data[i].split("do()")
            tmp.pop(0)
            for item in tmp:
                new_data.append(item)
    new_data = "".join(new_data)
    return part_1(new_data)


print("======== Part 2 ========")
print(part_2(data))
