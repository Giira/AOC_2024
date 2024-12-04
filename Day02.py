with open("Day02.txt") as f:
    data = [line.strip().split(" ") for line in f.readlines()]


def safe_report(report):
    # all() returns True if all iterables are True
    asc = all(0 < int(report[i+1]) - int(report[i]) <= 3 for i in range(len(report) - 1)) 
    desc = all(-3 <= int(report[i+1]) - int(report[i]) < 0 for i in range(len(report) - 1))
    if asc or desc:
        return True
    else:
        return False


def part_1(data):
    total_safe = 0
    for report in data:
        if safe_report(report):
            total_safe += 1
    return total_safe


total_safe = part_1(data)



def part_2(data):
    total_extra_safe = 0
    for report in data:
        if any(safe_report(report[:i] + report[i+1:]) for i in range(len(report) + 1)):
            total_extra_safe += 1
    return total_extra_safe


if __name__ == "__main__":
    print("======== Part 1 ========")
    print(part_1(data))

    print("======== Part 2 ========")
    print(part_2(data))
